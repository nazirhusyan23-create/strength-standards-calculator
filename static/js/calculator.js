(function () {
  "use strict";

  var page = document.querySelector(".calc-page");
  if (!page) return; // hub page — nothing to wire up

  var slug = page.dataset.slug;
  var inputType = page.dataset.inputType;
  var form = document.getElementById("calc-form");
  var errorEl = document.getElementById("form-error");
  var resultEl = document.getElementById("calc-result");
  var emptyEl = document.getElementById("calc-result-empty");
  var tierNameEl = document.getElementById("result-tier-name");
  var gaugeFill = document.getElementById("plate-gauge-fill");
  var gaugeSegs = document.querySelectorAll(".plate-gauge-seg");
  var progressNote = document.getElementById("result-progress-note");
  var statsEl = document.getElementById("result-stats");

  var TIER_ORDER = Array.from(gaugeSegs).map(function (s) { return s.dataset.tier; });

  function showError(msg) {
    errorEl.textContent = msg;
    errorEl.hidden = false;
  }
  function clearError() {
    errorEl.hidden = true;
    errorEl.textContent = "";
  }

  function gatherPayload() {
    var fd = new FormData(form);
    var sex = fd.get("sex") || "male";
    var unit = fd.get("unit") || "lb";
    var payload = { sex: sex, unit: unit };

    if (inputType === "reps_weighted") {
      payload.bodyweight = fd.get("bodyweight");
      payload.added_weight = fd.get("added_weight") || 0;
      payload.reps = fd.get("reps");
    } else if (inputType === "ratio_external") {
      payload.bodyweight = fd.get("bodyweight");
      payload.weight_lifted = fd.get("weight_lifted");
      payload.reps = fd.get("reps");
    } else if (inputType === "reps_only") {
      payload.bodyweight = fd.get("bodyweight");
      payload.reps = fd.get("reps");
      if (page.dataset.variantToggle) {
        payload.variant = fd.get("variant") || "wall";
      }
    } else if (inputType === "time_only") {
      payload.bodyweight = fd.get("bodyweight");
      payload.seconds = fd.get("seconds");
    }
    return payload;
  }

  function renderGauge(tierIndex, progressPct) {
    gaugeSegs.forEach(function (seg, i) {
      seg.classList.toggle("is-filled", i < tierIndex);
      seg.classList.toggle("is-current", i === tierIndex);
    });
    var segWidth = 100 / TIER_ORDER.length;
    var fillPct = segWidth * tierIndex + segWidth * (progressPct / 100);
    gaugeFill.style.width = Math.min(100, Math.max(0, fillPct)) + "%";
  }

  function statRow(label, value) {
    var dt = document.createElement("dt");
    dt.textContent = label;
    var dd = document.createElement("dd");
    dd.textContent = value;
    return [dt, dd];
  }

  function renderStats(data) {
    statsEl.innerHTML = "";
    var rows = [];

    if (data.metric === "ratio") {
      rows.push(statRow("Estimated 1RM", data.one_rm_lb + " lb / " + data.one_rm_kg + " kg"));
      rows.push(statRow("Ratio to bodyweight", data.ratio + "x"));
    } else if (data.metric === "reps") {
      rows.push(statRow("Reps", String(data.reps)));
    } else if (data.metric === "time") {
      rows.push(statRow("Hold time", data.seconds + " sec"));
    }

    rows.forEach(function (pair) {
      statsEl.appendChild(pair[0]);
      statsEl.appendChild(pair[1]);
    });
  }

  function renderProgressNote(data) {
    if (!data.next_tier) {
      progressNote.textContent = "You're at the top tier — Elite.";
      return;
    }
    var pct = data.progress_pct;
    var unitWord = "";
    if (data.metric === "ratio") unitWord = "x bodyweight";
    else if (data.metric === "reps") unitWord = " reps";
    else if (data.metric === "time") unitWord = " sec";

    var remaining = data.remaining_to_next;
    var remainingStr = (data.metric === "ratio")
      ? remaining.toFixed(2) + unitWord
      : Math.ceil(remaining) + unitWord;

    progressNote.textContent = "You're " + pct + "% through " + data.tier +
      " — about " + remainingStr + " more to reach " + data.next_tier + ".";
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    clearError();
    var payload = gatherPayload();

    fetch("/api/calculate/" + slug, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then(function (res) {
        return res.json().then(function (data) {
          return { ok: res.ok, data: data };
        });
      })
      .then(function (out) {
        if (!out.ok) {
          showError(out.data.error || "Something went wrong. Check your inputs.");
          return;
        }
        var data = out.data;
        emptyEl.hidden = true;
        resultEl.hidden = false;
        tierNameEl.textContent = data.tier;
        renderGauge(data.tier_index, data.progress_pct);
        renderProgressNote(data);
        renderStats(data);
      })
      .catch(function () {
        showError("Couldn't reach the calculator. Please try again.");
      });
  });

  // Standards table sex toggle
  var toggleBtns = document.querySelectorAll(".table-toggle-btn");
  var tableWraps = document.querySelectorAll(".standards-table-wrap");
  toggleBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var sex = btn.dataset.tableSex;
      toggleBtns.forEach(function (b) { b.classList.toggle("is-active", b === btn); });
      tableWraps.forEach(function (w) { w.hidden = w.dataset.tableFor !== sex; });
    });
  });

  // Keep table toggle in sync with the sex radio in the form
  var sexRadios = form.querySelectorAll('input[name="sex"]');
  sexRadios.forEach(function (r) {
    r.addEventListener("change", function () {
      var btn = document.querySelector('.table-toggle-btn[data-table-sex="' + r.value + '"]');
      if (btn) btn.click();
    });
  });

  // Added-weight field is optional for bodyweight-only lifts — no extra logic needed,
  // it already defaults to 0.
})();
