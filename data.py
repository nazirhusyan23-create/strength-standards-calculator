# -*- coding: utf-8 -*-
"""
Central config for all 15 Strength Standards Calculators.
Every page is generated from this file + templates/calculator.html,
so adding calculator #16 later just means adding a dict entry here.

Tier numbers are reasonable estimates assembled from the brief and
spot-checked against a couple of published strength-standards sites
(StrengthLevel-style bodyweight ratios, common calisthenics progression
charts). They are NOT authoritative — flagged again in README.md.

Each entry carries five kinds of copy, all unique per calculator (no
shared boilerplate strings) so every page stands on its own as real
content rather than a template with the noun swapped out:
  - intro            1-2 sentences under the H1
  - how_to_test       the correct way to actually perform the test
  - how_to_improve    concrete progression advice for this exact lift
  - faq               5 Q&A pairs specific to this movement
"""

INF = float("inf")

TIER_ORDER = ["Beginner", "Novice", "Intermediate", "Advanced", "Elite"]


def ratio_tiers(low_to_high):
    """low_to_high: list of 4 breakpoints -> builds 5 tier ranges."""
    b1, b2, b3, b4 = low_to_high
    return {
        "Beginner": [0, b1],
        "Novice": [b1, b2],
        "Intermediate": [b2, b3],
        "Advanced": [b3, b4],
        "Elite": [b4, INF],
    }


CALCULATORS = {

    # ---------------------------------------------------------------- 1
    "pull-up": {
        "name": "Pull-up",
        "short": "Pull-up",
        "category": "Vertical pull",
        "seo_keywords": {
            "primary": "pull up calculator",
            "secondary": ["how many pull ups is good", "average pull ups for my weight"],
        },
        "input_type": "reps_weighted",  # bodyweight + optional added weight + reps
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([0.8, 1.0, 1.3, 1.6]),
            "female": ratio_tiers([0.48, 0.6, 0.78, 0.96]),
        },
        "intro": "The pull-up calculator estimates your one-rep max pulling "
                 "strength from your bodyweight, any added weight, and the "
                 "reps you performed, then ranks it against lifters of your "
                 "sex as a multiple of bodyweight.",
        "how_to_test": "Hang from a bar with an overhand grip, hands just "
                 "outside shoulder width, arms fully extended (dead hang). "
                 "Pull until your chin clears the bar, then lower under "
                 "control back to a full hang — that's one rep. Kipping, "
                 "swinging, or stopping short of a full hang or full chin "
                 "clearance inflates the count, so test on a clean set "
                 "taken close to failure.",
        "how_to_improve": "If you can't yet do a full rep, build the hang "
                 "and the negative first: jump or step to the top position "
                 "and lower yourself as slowly as possible for 3-5 reps. "
                 "Once you have 3-5 strict reps, add volume with sets "
                 "spread across the week before chasing more reps in a "
                 "single set, and add weight only once 12+ strict reps "
                 "feel controlled.",
        "faq": [
            ("What is a good pull-up number?",
             "For most men, doing 8-12 strict pull-ups at bodyweight lands "
             "in the Intermediate-to-Advanced range. For most women, 4-8 "
             "strict reps is a comparable milestone."),
            ("Do added-weight pull-ups count differently?",
             "No — the calculator converts bodyweight plus any added "
             "weight into an estimated one-rep max, so a few reps with "
             "extra weight and many reps at bodyweight can land in the "
             "same tier."),
            ("How many reps should I enter?",
             "Enter reps from a single clean, full-range set taken close "
             "to failure. The formula is most accurate under 12 reps."),
            ("Does grip width change the standard?",
             "A shoulder-width overhand grip is the reference used here. "
             "A wider grip is usually a little harder and a closer, "
             "neutral, or underhand grip is usually a little easier, so "
             "treat your tier as an estimate if you use a very different "
             "grip."),
            ("Why does the calculator ask for my sex?",
             "Average upper-body strength relative to bodyweight differs "
             "between men and women, so each tier uses its own thresholds "
             "rather than one shared scale — that keeps the comparison "
             "fair rather than penalizing one group by default."),
        ],
    },

    # ---------------------------------------------------------------- 2
    "chin-up": {
        "name": "Chin-up",
        "short": "Chin-up",
        "category": "Vertical pull",
        "seo_keywords": {
            "primary": "chin up calculator",
            "secondary": ['how many chin ups is good', 'chin up vs pull up which is easier'],
        },
        "input_type": "reps_weighted",
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([0.72, 0.9, 1.17, 1.44]),
            "female": ratio_tiers([0.43, 0.54, 0.7, 0.86]),
        },
        "intro": "Chin-ups (underhand grip) recruit more biceps than "
                 "pull-ups and are typically 10-20% easier, so this "
                 "calculator uses slightly lower bodyweight-ratio "
                 "thresholds for each tier.",
        "how_to_test": "Grip the bar underhand (palms facing you), hands "
                 "about shoulder width apart, and start from a full dead "
                 "hang. Pull until your chin clears the bar and lower back "
                 "to a complete hang each rep. Keep the ribs down and avoid "
                 "excessive backward lean, which turns the pull into a "
                 "row and makes the rep easier than it should be.",
        "how_to_improve": "Because the biceps assist more here, chin-ups "
                 "are a good entry point if a strict pull-up is still out "
                 "of reach. Build reps on chin-ups first, then transfer "
                 "that pulling strength to pull-ups by swapping in a few "
                 "overhand-grip sets once you can do 8-10 strict chin-ups "
                 "comfortably.",
        "faq": [
            ("Is a chin-up easier than a pull-up?",
             "Yes, for most people — the underhand grip biases the "
             "biceps more, which usually adds a rep or two at the same "
             "difficulty level."),
            ("What is a good chin-up number?",
             "Ten or more strict chin-ups at bodyweight is a strong, "
             "Advanced-level result for most men; five or more is a "
             "strong result for most women."),
            ("Should I train chin-ups or pull-ups first?",
             "Either is fine as a base — many lifters build the chin-up "
             "first since the biceps assist more, then progress to "
             "strict pull-ups."),
            ("Do chin-ups build the back as much as pull-ups?",
             "Both hit the lats hard, but chin-ups shift more work onto "
             "the biceps and pull-ups keep slightly more tension on the "
             "back and rear shoulders — training both grips covers the "
             "gap."),
            ("Can I mix chin-ups and pull-ups in the same test set?",
             "No — enter reps from one grip only. Mixing grips mid-set "
             "changes the difficulty partway through and won't match "
             "either calculator's standards accurately."),
        ],
    },

    # ---------------------------------------------------------------- 3
    "dip": {
        "name": "Dip",
        "short": "Dip",
        "category": "Horizontal push",
        "seo_keywords": {
            "primary": "dip calculator",
            "secondary": ['how many dips is good', 'good dip weight for bodyweight'],
        },
        "input_type": "reps_weighted",
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([0.9, 1.1, 1.4, 1.7]),
            "female": ratio_tiers([0.52, 0.64, 0.81, 0.99]),
        },
        "intro": "The dip calculator estimates your one-rep max pressing "
                 "strength on parallel bars from bodyweight, added weight, "
                 "and reps, then compares it to other lifters as a "
                 "multiple of bodyweight.",
        "how_to_test": "On parallel bars, lower under control until your "
                 "shoulders drop below your elbows, then press back to "
                 "full lockout — that full range is what separates a real "
                 "dip from a half-rep. Keep a slight forward lean to "
                 "protect the shoulders and avoid flaring the elbows out "
                 "wide, which shifts load off the triceps and chest.",
        "how_to_improve": "If bodyweight dips aren't there yet, use an "
                 "assisted-dip machine or a resistance band looped over "
                 "the bars to reduce the load while keeping full range of "
                 "motion. Once you can do 12-15 strict bodyweight reps, "
                 "start adding small increments of weight on a belt to "
                 "keep building without sacrificing depth.",
        "faq": [
            ("What is a good dip number?",
             "Fifteen or more strict bodyweight dips is a strong, "
             "Advanced-level result for most men; the equivalent for most "
             "women is closer to eight to twelve reps."),
            ("Are ring dips the same as bar dips?",
             "No — rings add instability and reduce your effective "
             "strength, which is why this suite has a separate ring-dip "
             "calculator with lower thresholds."),
            ("How deep should the dip go?",
             "Use a full range of motion: shoulders below elbows at the "
             "bottom. Partial-range dips will inflate your number."),
            ("Should I feel this more in my chest or triceps?",
             "Both work together, but a slight forward torso lean shifts "
             "more emphasis to the chest, while staying upright with "
             "elbows close to the body shifts more emphasis to the "
             "triceps — either is fine for this calculator as long as "
             "depth and lockout are consistent."),
            ("Is dip strength related to bench press strength?",
             "They're correlated since both are horizontal/vertical "
             "pressing movements, but dips add more shoulder-stability "
             "demand, so a strong bench doesn't automatically mean a "
             "strong dip and vice versa."),
        ],
    },

    # ---------------------------------------------------------------- 4
    "push-up": {
        "name": "Push-up",
        "short": "Push-up",
        "category": "Horizontal push",
        "seo_keywords": {
            "primary": "push up calculator",
            "secondary": ['how many push ups is good for my age', 'average push ups by age'],
        },
        "input_type": "reps_only",
        "unit_label": "reps",
        "tiers": {
            "male": ratio_tiers([10, 20, 40, 60]),
            "female": ratio_tiers([5, 15, 25, 40]),
        },
        "intro": "The push-up calculator ranks strict, full-range push-ups "
                 "performed in one set against typical standards for your "
                 "sex — no added weight needed, just reps.",
        "how_to_test": "Start in a straight-arm plank, hands roughly under "
                 "the shoulders. Lower until your chest is near the floor, "
                 "keeping hips and shoulders in one straight line, then "
                 "press back to a full elbow lockout. Do the whole set at "
                 "a steady, controlled tempo and stop the count the moment "
                 "your hips sag or you can no longer reach full depth.",
        "how_to_improve": "If a full set is hard to string together, try "
                 "an incline push-up (hands on a bench or step) to reduce "
                 "the load while keeping the same strict range of motion, "
                 "then lower the incline as reps improve. To push past a "
                 "plateau at bodyweight, add a weighted vest or a slow "
                 "3-second lowering phase to build strength beyond what "
                 "reps alone target.",
        "faq": [
            ("What is a good push-up number?",
             "Forty or more strict push-ups in one set is a strong, "
             "Advanced-level result for most men; twenty-five or more is "
             "a strong result for most women."),
            ("Does form affect the count?",
             "Yes — a strict push-up means chest to near the floor, full "
             "elbow lockout, and a straight body line. Sagging hips or "
             "partial reps don't count toward an honest total."),
            ("How is this different from a fitness test max?",
             "Most standardized tests (military, police) allow some form "
             "breakdown near failure; this calculator assumes strict form "
             "throughout, so its tiers run a little stricter."),
            ("Does hand placement matter?",
             "A standard shoulder-width placement is the reference here. "
             "A wider hand position emphasizes the chest and is slightly "
             "easier for most people; a narrower, triceps-focused "
             "placement is usually a bit harder at the same rep count."),
            ("Should I test push-ups to complete failure?",
             "Test to the point where you can no longer hold strict form "
             "rather than grinding out sloppy reps afterward — a few "
             "clean reps give a more honest number than extra reps with "
             "breakdown."),
        ],
    },

    # ---------------------------------------------------------------- 5
    "bench-press": {
        "name": "Bench Press",
        "short": "Bench press",
        "category": "Barbell push",
        "seo_keywords": {
            "primary": "bench press calculator",
            "secondary": ['is bench pressing bodyweight good', 'bench press standards by weight'],
        },
        "input_type": "ratio_external",  # weight lifted + reps, ratio to bodyweight
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([0.5, 0.75, 1.25, 1.75]),
            "female": ratio_tiers([0.25, 0.5, 0.75, 1.0]),
        },
        "intro": "The bench press calculator estimates your one-rep max "
                 "from the weight and reps of a recent set, then expresses "
                 "it as a multiple of bodyweight against standard tiers.",
        "how_to_test": "Lie flat on the bench with feet planted, a natural "
                 "arch, and shoulder blades pulled together and down. "
                 "Lower the bar under control to touch the chest, pause "
                 "briefly, then press to full lockout without bouncing off "
                 "the chest or lifting the hips off the bench. Use a set "
                 "of 1-8 reps taken close to failure for the most accurate "
                 "1RM estimate.",
        "how_to_improve": "Bench press strength usually stalls on either "
                 "the bottom (off the chest) or the lockout — track where "
                 "your sets slow down and add a targeted accessory: "
                 "close-grip bench or paused reps for a weak bottom, "
                 "overhead press or triceps work for a weak lockout. "
                 "Progressing the working weight by small increments "
                 "(2.5-5 lb) most sessions compounds faster than chasing "
                 "big jumps.",
        "faq": [
            ("What is a good bench press?",
             "Benching bodyweight for reps is a common Intermediate "
             "milestone for men; 1.25x bodyweight and up is Advanced. "
             "For women, bodyweight is closer to Elite territory."),
            ("Why does the calculator ask for bodyweight?",
             "Absolute weight on the bar doesn't tell the whole story — "
             "expressing your 1RM as a ratio of bodyweight lets you "
             "compare fairly across different body sizes."),
            ("How accurate is the 1RM estimate?",
             "The Epley formula used here is a solid estimate up to about "
             "10-12 reps; beyond that, accuracy drops, so the calculator "
             "caps reps at 12."),
            ("Does a leg drive or arch change what counts?",
             "A moderate, controlled arch and leg drive are part of a "
             "standard competition-style bench and are fine to include — "
             "just keep the hips on the bench throughout the rep."),
            ("Why is bench press lower than squat or deadlift ratios?",
             "Pressing is limited by smaller muscle groups (chest, "
             "shoulders, triceps) working against a load your whole "
             "upper body has to stabilize, while squats and deadlifts "
             "recruit the much larger posterior-chain and leg muscles."),
        ],
    },

    # ---------------------------------------------------------------- 6
    "squat": {
        "name": "Squat",
        "short": "Squat",
        "category": "Barbell lower body",
        "seo_keywords": {
            "primary": "squat calculator",
            "secondary": ['is 1.5x bodyweight squat good', 'squat standards for beginners'],
        },
        "input_type": "ratio_external",
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([0.75, 1.25, 1.5, 2.0]),
            "female": ratio_tiers([0.5, 0.75, 1.25, 1.5]),
        },
        "intro": "The squat calculator estimates your one-rep max back "
                 "squat from a recent set's weight and reps, then ranks it "
                 "against standard bodyweight-ratio tiers.",
        "how_to_test": "Set the bar across the upper back, brace your "
                 "core, and squat until the hip crease drops below the top "
                 "of the knee (at least parallel), then drive back to "
                 "standing without your knees caving inward or your lower "
                 "back rounding. Use a recent working set of 1-8 reps "
                 "close to failure — old numbers from months ago will "
                 "give a stale estimate.",
        "how_to_improve": "Most squat plateaus come from either weak "
                 "quads out of the bottom or a weak, rounding back — front "
                 "squats and pause squats target the first, while good "
                 "mornings and heavier deadlift-pattern work target the "
                 "second. Also check depth on video occasionally; a squat "
                 "that quietly gets shallower over time inflates numbers "
                 "without real strength gains behind them.",
        "faq": [
            ("What is a good squat?",
             "Squatting 1.5x bodyweight is a strong Advanced result for "
             "most men; for most women, 1.25x bodyweight sits in the same "
             "range."),
            ("Does squat depth matter for this calculator?",
             "Yes — enter your best weight for a rep performed at least "
             "to parallel. Partial squats will overstate your true "
             "strength."),
            ("Front squat or back squat?",
             "This calculator assumes back squat, which is typically "
             "heavier than a front squat at the same effort level."),
            ("Does stance width change the standard?",
             "A moderate, athletic stance is the reference. A wide "
             "powerlifting-style stance can move slightly more weight for "
             "some lifters, so treat the tier as an estimate if your "
             "stance is unusually wide or narrow."),
            ("Why is my squat weaker than my deadlift?",
             "That's normal for most lifters — the squat has a longer "
             "range of motion under load and a harder sticking point out "
             "of the bottom, so it's common to deadlift noticeably more "
             "than you squat."),
        ],
    },

    # ---------------------------------------------------------------- 7
    "deadlift": {
        "name": "Deadlift",
        "short": "Deadlift",
        "category": "Barbell lower body",
        "seo_keywords": {
            "primary": "deadlift calculator",
            "secondary": ['is 2x bodyweight deadlift good', 'deadlift standards by bodyweight'],
        },
        "input_type": "ratio_external",
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([1.0, 1.5, 2.0, 2.5]),
            "female": ratio_tiers([0.75, 1.25, 1.75, 2.0]),
        },
        "intro": "The deadlift calculator estimates your one-rep max from "
                 "a recent working set, then compares it to other lifters "
                 "of your sex as a multiple of bodyweight.",
        "how_to_test": "Set up with the bar over mid-foot, grip just "
                 "outside the legs, back flat and braced. Drive through "
                 "the floor to stand fully upright with hips and knees "
                 "locked out, then lower under control. A rounded lower "
                 "back or a bar that drifts far out in front usually means "
                 "the weight was too heavy for clean form that day, so "
                 "test from a set where form held throughout.",
        "how_to_improve": "If the bar stalls just off the floor, work on "
                 "starting-strength drills like deficit deadlifts or "
                 "pause deadlifts just above the ground. If it stalls near "
                 "lockout, target the glutes and upper back with Romanian "
                 "deadlifts and rows. Deadlifts also recover slowly for "
                 "most people, so heavy singles once a week with lighter "
                 "volume work on other days tends to progress better than "
                 "maxing out every session.",
        "faq": [
            ("What is a good deadlift?",
             "Pulling 2x bodyweight is a widely-used Advanced milestone "
             "for men; for women, 1.75x bodyweight lands in a similar "
             "range."),
            ("Conventional or sumo deadlift?",
             "Either stance works for this calculator — enter the best "
             "weight and reps from whichever stance you compete in or "
             "train most."),
            ("Why is the deadlift ratio higher than squat or bench?",
             "The deadlift starts from a dead stop with a shorter range "
             "of motion for most lifters, which generally allows heavier "
             "loads relative to bodyweight."),
            ("Does grip style (mixed, hook, double overhand) matter?",
             "Grip style affects how much weight you can hold, not the "
             "underlying pulling strength this calculator estimates, so "
             "any grip you can complete the rep with is fine to enter."),
            ("Should I include straps or a belt?",
             "If that's how you train and compete, enter that number as "
             "your working set — the calculator ranks the weight you can "
             "actually move, however you support the grip or the trunk."),
        ],
    },

    # ---------------------------------------------------------------- 8
    "overhead-press": {
        "name": "Overhead Press",
        "short": "Overhead press",
        "category": "Barbell push",
        "seo_keywords": {
            "primary": "overhead press calculator",
            "secondary": ['how much should i overhead press', 'ohp bodyweight ratio'],
        },
        "input_type": "ratio_external",
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([0.35, 0.55, 0.8, 1.0]),
            "female": ratio_tiers([0.2, 0.35, 0.5, 0.65]),
        },
        "intro": "The overhead press calculator estimates your strict "
                 "standing one-rep max from a recent set, then ranks it as "
                 "a multiple of bodyweight.",
        "how_to_test": "Standing with the bar at shoulder height, brace "
                 "your core and glutes, then press straight overhead to "
                 "full lockout with the bar finishing over the middle of "
                 "the foot, without bending the knees or leaning back "
                 "excessively to launch the bar. Test with a strict set of "
                 "1-8 reps — any noticeable leg dip turns the lift into a "
                 "push press and won't match this calculator's standards.",
        "how_to_improve": "Overhead pressing strength is often limited by "
                 "shoulder mobility and core stability as much as raw "
                 "pushing power, so pair heavy pressing days with "
                 "dedicated core bracing work and thoracic mobility "
                 "drills. Because the ratios here are demanding, steady "
                 "progress of a few pounds every few weeks is realistic — "
                 "expecting bench-press-like jumps will lead to form "
                 "breakdown.",
        "faq": [
            ("What is a good overhead press?",
             "Pressing bodyweight overhead for a single strict rep is a "
             "rare, Elite-level feat for most men; for women, around "
             "0.65x bodyweight lands in the same territory."),
            ("Strict press or push press?",
             "This calculator assumes a strict press with no leg drive. "
             "A push press number will overstate your strict strength."),
            ("Why are overhead press ratios so much lower than bench?",
             "Pressing overhead against full bodyweight-supported gravity "
             "with no leg or bench assistance is mechanically much harder, "
             "so the ratios run lower across every tier."),
            ("Does starting position (from the rack vs. from the floor) matter?",
             "Starting from a rack at shoulder height is the standard "
             "reference. Cleaning the bar to the shoulders first adds "
             "fatigue before the press, which can lower the number you'd "
             "otherwise hit fresh."),
            ("Is overhead press good for shoulder health?",
             "Strict pressing with full range of motion is generally good "
             "for shoulder strength and stability when programmed "
             "sensibly, but anyone with existing shoulder pain should get "
             "it checked before loading it heavily."),
        ],
    },

    # ---------------------------------------------------------------- 9
    "muscle-up": {
        "name": "Muscle-up",
        "short": "Muscle-up",
        "category": "Vertical pull",
        "seo_keywords": {
            "primary": "muscle up calculator",
            "secondary": ['how many muscle ups is good', 'muscle up progression standards'],
        },
        "input_type": "reps_only",
        "unit_label": "reps",
        "tiers": {
            "male": ratio_tiers([1, 4, 8, 13]),
            "female": ratio_tiers([1, 2, 5, 9]),
        },
        "intro": "The muscle-up calculator ranks strict bar or ring "
                 "muscle-ups performed in one set — a movement that "
                 "combines a pull-up with a dip, so even one clean rep is "
                 "a meaningful milestone.",
        "how_to_test": "From a dead hang, pull explosively while leaning "
                 "slightly forward so your chest drives toward the bar, "
                 "transition your wrists over the top without a kip or leg "
                 "swing for momentum, then press out to full lockout above "
                 "the bar or rings. Count only reps where the transition "
                 "comes from control and timing rather than a big lower-body "
                 "swing.",
        "how_to_improve": "Build the two halves separately before "
                 "chasing full reps: high pull-ups where the chest reaches "
                 "bar height, and dips with full lockout, both for solid "
                 "sets of 8-10. Then practice the transition itself with "
                 "a slightly lower bar or a resistance band for assistance "
                 "until the timing clicks and you can link pull, "
                 "transition, and dip into one motion.",
        "faq": [
            ("What is a good muscle-up number?",
             "Eight or more strict muscle-ups in a set is a strong, "
             "Advanced-level result for most men; five or more is a "
             "strong result for most women."),
            ("What counts as a strict muscle-up?",
             "No kipping or leg swing — the transition from pull to dip "
             "should come from upper-body strength and control."),
            ("Do I need to be able to do a pull-up first?",
             "Yes — most people need well over ten strict pull-ups and "
             "several dips before a first muscle-up becomes realistic."),
            ("Are ring muscle-ups harder than bar muscle-ups?",
             "Yes, generally — rings add instability through the "
             "transition, so this calculator's thresholds are a "
             "reasonable estimate for either, but expect ring reps to "
             "feel harder at the same count."),
            ("Why does even one rep count for something on this scale?",
             "The muscle-up combines two hard movements into one "
             "continuous, coordinated motion, so a single strict rep "
             "already represents a real strength and skill threshold — "
             "that's why the Beginner tier here starts at just one rep."),
        ],
    },

    # ---------------------------------------------------------------- 10
    "pistol-squat": {
        "name": "Pistol Squat",
        "short": "Pistol squat",
        "category": "Single-leg lower body",
        "seo_keywords": {
            "primary": "pistol squat calculator",
            "secondary": ['how many pistol squats is good', 'pistol squat per leg standard'],
        },
        "input_type": "reps_only",
        "unit_label": "reps per leg",
        "tiers": {
            "male": ratio_tiers([2, 6, 11, 20]),
            "female": ratio_tiers([1, 4, 9, 16]),
        },
        "intro": "The pistol squat calculator ranks strict, full-depth "
                 "single-leg squats performed per leg in one set — a test "
                 "of single-leg strength, balance, and mobility together.",
        "how_to_test": "Standing on one leg with the other extended in "
                 "front, lower under control until the hips drop below "
                 "the knee of the working leg, then stand back up without "
                 "using the free leg for a push off the ground or losing "
                 "balance. Count only reps completed on each leg "
                 "separately, since strength and control commonly differ "
                 "side to side.",
        "how_to_improve": "Ankle and hip mobility limit most people before "
                 "raw leg strength does, so mobility work is often the "
                 "fastest route to a first rep. Build toward it with "
                 "box or bench pistol squats (reducing depth), assisted "
                 "pistols holding a rail or a band for balance, and single-leg "
                 "step-downs — narrowing the assistance gradually until "
                 "you can control the full range unaided.",
        "faq": [
            ("What is a good pistol squat number?",
             "Eleven or more strict reps per leg is a strong, "
             "Advanced-level result for most men; nine or more is a "
             "strong result for most women."),
            ("What counts as full depth?",
             "Hips below the knee of the working leg, with control on "
             "the way down and up — no bouncing out of the bottom."),
            ("Why is one leg so much harder than a bodyweight squat?",
             "A pistol squat puts the full bodyweight load, balance "
             "demand, and ankle/hip mobility requirement onto a single "
             "leg, which is far more demanding than a two-leg squat."),
            ("Do both legs need to hit the same number?",
             "No — enter your weaker leg's rep count for an honest tier, "
             "since most people have a meaningful side-to-side "
             "difference and the weaker side is the real limiting "
             "factor."),
            ("Can I hold a counterweight to help balance?",
             "Holding something light for counterbalance is a common "
             "learning aid, but for testing your true number, perform the "
             "set unassisted so the reps reflect strength and balance "
             "rather than an external aid."),
        ],
    },

    # ---------------------------------------------------------------- 11
    "ring-dip": {
        "name": "Ring Dip",
        "short": "Ring dip",
        "category": "Horizontal push",
        "seo_keywords": {
            "primary": "ring dip calculator",
            "secondary": ['ring dip vs bar dip standards', 'how many ring dips is good'],
        },
        "input_type": "reps_weighted",
        "unit_label": "x bodyweight (1RM)",
        "tiers": {
            "male": ratio_tiers([0.7, 0.9, 1.2, 1.5]),
            "female": ratio_tiers([0.4, 0.52, 0.7, 0.87]),
        },
        "intro": "Ring dips add instability on top of the standard dip, so "
                 "this calculator uses lower bodyweight-ratio thresholds "
                 "for every tier to account for the extra difficulty.",
        "how_to_test": "Support yourself on rings with arms locked and "
                 "the rings turned out slightly (support position), lower "
                 "under control until shoulders drop below elbows while "
                 "keeping the rings from drifting apart, then press back "
                 "to full lockout. Keep the swing to a minimum — visible "
                 "kipping or rings swinging wildly means the set won't "
                 "reflect true pressing strength.",
        "how_to_improve": "Ring stability usually needs its own practice "
                 "separate from raw pressing strength — spend time simply "
                 "holding the top support position (an L-sit-style hold "
                 "with locked arms) before adding reps. Building a strong "
                 "bar-dip base first, then transferring to rings with "
                 "lower reps and a focus on control over speed, is the "
                 "most reliable path.",
        "faq": [
            ("Why are ring dip standards lower than bar dips?",
             "Rings move under you, forcing the shoulders and stabilizer "
             "muscles to work much harder to control the same range of "
             "motion, which reduces the weight or reps most people can "
             "manage."),
            ("What is a good ring dip number?",
             "Twelve or more strict ring dips at bodyweight is a strong, "
             "Advanced-level result for most men."),
            ("Should I master bar dips first?",
             "It helps — a solid bar dip base (around 10-15 reps) makes "
             "the added instability of rings much more manageable."),
            ("Do the rings need to be turned out?",
             "A slight external rotation (turnout) at the top is the "
             "standard reference position and is easier on the shoulders "
             "— straight rings without turnout are typically a bit "
             "harder to stabilize at the same rep count."),
            ("Is added weight realistic on rings?",
             "Yes, once bodyweight ring dips are very controlled — but "
             "add small increments and prioritize keeping the rings "
             "stable, since instability compounds quickly once external "
             "load is added."),
        ],
    },

    # ---------------------------------------------------------------- 12
    "weighted-pull-up": {
        "name": "Weighted Pull-up",
        "short": "Weighted pull-up",
        "category": "Vertical pull",
        "seo_keywords": {
            "primary": "weighted pull up calculator",
            "secondary": ['how much weight to add to pull ups', 'weighted pull up standards by bodyweight'],
        },
        "input_type": "reps_weighted",
        "unit_label": "x bodyweight (1RM)",
        "always_show_added_weight": True,
        "tiers": {
            "male": ratio_tiers([0.8, 1.0, 1.3, 1.6]),
            "female": ratio_tiers([0.48, 0.6, 0.78, 0.96]),
        },
        "intro": "Already doing strict bodyweight pull-ups comfortably? "
                 "This calculator focuses on how much extra weight to add "
                 "and estimates your true one-rep max pulling strength "
                 "from that loaded set.",
        "how_to_test": "Attach weight with a dip belt or a sturdy vest so "
                 "your grip and hang aren't compromised, then perform the "
                 "same strict pull-up standard as bodyweight reps: full "
                 "hang to chin over the bar, no kipping. Test with a "
                 "weight and rep combination that stays under about 8 "
                 "reps for the most accurate one-rep max estimate.",
        "how_to_improve": "Progress the load in small, consistent jumps "
                 "(2.5-5 lb) rather than big leaps, and keep some lighter, "
                 "higher-rep bodyweight pull-up sets in the week to "
                 "maintain volume and technique. If reps drop below 3-4 "
                 "at a given weight, hold there for a few sessions before "
                 "adding more — grip and connective tissue often need "
                 "extra time to catch up to pulling strength.",
        "faq": [
            ("How much weight should I add?",
             "As a rough guide, once you can do 12+ strict bodyweight "
             "pull-ups, start adding 5-10% of bodyweight and build reps "
             "back up from there."),
            ("Does this use the same formula as the pull-up calculator?",
             "Yes — bodyweight plus added weight feeds the same one-rep "
             "max formula, so the two calculators share identical tier "
             "thresholds."),
            ("What is a good weighted pull-up number?",
             "Adding 50% of bodyweight for a single strict rep is a "
             "strong, Advanced-to-Elite result for most men."),
            ("Belt or vest — does it matter which I use?",
             "Not for the calculator itself; enter whatever total added "
             "weight you used. A belt is usually more comfortable for "
             "heavier loads, while a vest can be easier to manage for "
             "lighter added weight."),
            ("My grip fails before my back does — what should I do?",
             "That's common at higher added weights. Dedicated grip and "
             "forearm work, or using straps occasionally to push back "
             "strength without a grip ceiling, can help the numbers "
             "you enter here reflect true pulling strength."),
        ],
    },

    # ---------------------------------------------------------------- 13
    "l-sit": {
        "name": "L-sit",
        "short": "L-sit",
        "category": "Isometric hold",
        "seo_keywords": {
            "primary": "l sit calculator",
            "secondary": ['how long should an l sit be', 'average l sit hold time'],
        },
        "input_type": "time_only",  # hold time in seconds
        "unit_label": "seconds",
        "tiers": {
            "male": ratio_tiers([5, 15, 30, 60]),
            "female": ratio_tiers([3, 10, 20, 40]),
        },
        "intro": "The L-sit calculator ranks your best strict hold time "
                 "on parallettes, rings, or the floor — a pure test of "
                 "core and hip-flexor strength with no reps involved.",
        "how_to_test": "Support yourself on parallettes, blocks, or the "
                 "floor with arms locked and shoulders depressed, then "
                 "lift both legs straight out in front, parallel to the "
                 "ground, toes pointed. Start the timer the instant your "
                 "feet leave the floor and stop it the moment your hips "
                 "or knees bend, your legs drop below parallel, or you "
                 "touch down.",
        "how_to_improve": "Tucked holds (knees pulled to the chest instead "
                 "of legs extended) build the same shoulder and core "
                 "strength with far less hip-flexor and hamstring demand, "
                 "so they're the standard entry point. Progress from "
                 "tuck, to one-leg-extended, to full L-sit as hold time "
                 "improves, and train hip-flexor and hamstring flexibility "
                 "alongside strength — tight hamstrings are a common "
                 "limiter even for people with plenty of core strength.",
        "faq": [
            ("What is a good L-sit hold?",
             "Holding 30 seconds or more is a strong, Advanced-level "
             "result for most men; 20 seconds or more is a strong result "
             "for most women."),
            ("Does the hold have to be full L-sit?",
             "This calculator assumes legs held parallel to the floor. A "
             "tucked or one-leg-extended hold is easier and will "
             "overstate your tier."),
            ("How do I time it correctly?",
             "Start the clock the instant your feet leave the ground and "
             "stop it the moment form breaks down or you touch down."),
            ("Can I break up the hold into multiple short attempts?",
             "No — enter your single longest continuous hold. Adding up "
             "several short attempts doesn't reflect the same sustained "
             "core and shoulder demand as one unbroken hold."),
            ("Why do L-sit standards use seconds instead of reps?",
             "It's an isometric (static) hold rather than a repeated "
             "movement, so total time under tension is the meaningful "
             "measure of strength here, the same way a plank is timed "
             "rather than counted in reps."),
        ],
    },

    # ---------------------------------------------------------------- 14
    "handstand-push-up": {
        "name": "Handstand Push-up",
        "short": "Handstand push-up",
        "category": "Vertical push",
        "seo_keywords": {
            "primary": "handstand push up calculator",
            "secondary": ['how many handstand push ups is good', 'freestanding vs wall hspu standards'],
        },
        "input_type": "reps_only",
        "unit_label": "reps",
        "has_variant_toggle": True,  # wall-assisted vs freestanding
        "tiers": {
            "male": {
                "wall": ratio_tiers([3, 7, 13, 20]),
                "freestanding": ratio_tiers([2, 4, 7, 10]),
            },
            "female": {
                "wall": ratio_tiers([2, 4, 8, 12]),
                "freestanding": ratio_tiers([1, 2, 4, 6]),
            },
        },
        "intro": "The handstand push-up calculator ranks strict reps in "
                 "one set, with a toggle for wall-assisted versus "
                 "freestanding — freestanding is far harder at the same "
                 "rep count, so it uses its own, lower thresholds.",
        "how_to_test": "In a handstand against a wall (or freestanding, "
                 "balanced), lower your head toward the floor under "
                 "control until it lightly touches or comes close, then "
                 "press back to full elbow lockout without walking the "
                 "feet down the wall or breaking the handstand line. "
                 "Select the matching variant toggle before entering reps "
                 "so the result compares against the right standard.",
        "how_to_improve": "Build pressing range gradually with a pike "
                 "push-up progression (feet elevated, hips high) before "
                 "moving to a wall handstand, and add a folded mat or "
                 "small block to reduce range of motion at first if a "
                 "full head-to-floor rep isn't there yet. Freestanding "
                 "balance is a separate skill from pressing strength — "
                 "practice freestanding holds on their own before "
                 "expecting freestanding reps to match your wall numbers.",
        "faq": [
            ("What is a good handstand push-up number?",
             "Thirteen or more wall-assisted reps is a strong, "
             "Advanced-level result for most men; freestanding, seven or "
             "more reps reaches the same level."),
            ("Why is freestanding so much harder?",
             "Without the wall, you're also balancing the entire "
             "movement, which taxes coordination and stabilizers on top "
             "of raw pressing strength."),
            ("What counts as a strict rep?",
             "Head to floor (or close to it) at the bottom, and full "
             "elbow lockout at the top, in a controlled tempo."),
            ("Chest-facing wall or back-facing wall?",
             "Either setup is common for wall-assisted reps; enter your "
             "count regardless of which you use, since the calculator's "
             "wall-assisted tier is a general reference for supported "
             "handstand pressing."),
            ("Do I need a full freestanding handstand hold before HSPU?",
             "A solid, controlled freestanding handstand hold (ideally "
             "30+ seconds) is a reasonable prerequisite before attempting "
             "freestanding reps, since losing balance mid-press is both "
             "harder to recover from and riskier than losing a plain "
             "hold."),
        ],
    },

    # ---------------------------------------------------------------- 15
    "bulgarian-split-squat": {
        "name": "Bulgarian Split Squat",
        "short": "Bulgarian split squat",
        "category": "Single-leg lower body",
        "seo_keywords": {
            "primary": "bulgarian split squat calculator",
            "secondary": ['good bulgarian split squat weight', 'bss standards per leg'],
        },
        "input_type": "ratio_external",  # weight lifted, reps per leg
        "unit_label": "x bodyweight (1RM, per leg)",
        "faq_reps_note": "per leg",
        "tiers": {
            "male": ratio_tiers([0.3, 0.5, 0.75, 1.0]),
            "female": ratio_tiers([0.2, 0.35, 0.5, 0.65]),
        },
        "intro": "The Bulgarian split squat calculator estimates your "
                 "per-leg one-rep max from the weight (dumbbells, "
                 "kettlebells, or barbell) and reps of a recent set, then "
                 "ranks it as a multiple of bodyweight.",
        "how_to_test": "With the rear foot elevated on a bench and the "
                 "front foot far enough forward that the front knee stays "
                 "roughly over the ankle, lower until the rear knee "
                 "approaches the floor, then drive up through the front "
                 "heel to standing. Keep the torso reasonably upright and "
                 "test the same weight and rep count on both legs so any "
                 "side-to-side gap shows up clearly.",
        "how_to_improve": "Balance often limits load before leg strength "
                 "does, especially early on — holding light dumbbells at "
                 "your sides instead of a barbell on the back reduces the "
                 "stability demand while you build the pattern. Once the "
                 "movement feels controlled, progress load steadily on "
                 "your weaker leg specifically, since most people carry a "
                 "meaningful strength gap between sides that a symmetric "
                 "exercise like a back squat can hide.",
        "faq": [
            ("What is a good Bulgarian split squat?",
             "Loading 75% of bodyweight (combined, if using two "
             "dumbbells) for a single rep per leg is a strong, "
             "Advanced-level result for most men."),
            ("How do I enter the weight if I'm using two dumbbells?",
             "Enter the combined total of both dumbbells — the "
             "calculator treats it as one external load added to your "
             "front leg's work."),
            ("Why is this so much lower than a regular back squat?",
             "All the load sits on one leg with the rear leg only "
             "providing light balance assistance, which sharply reduces "
             "how much weight most people can handle compared to a "
             "two-leg squat."),
            ("Does rear-foot elevation height matter?",
             "A standard bench height (roughly knee height) is the "
             "reference used here. A much higher or lower elevation "
             "changes the range of motion and difficulty, so keep it "
             "consistent between tests if you want to track progress "
             "over time."),
            ("Should I test both legs even if one feels obviously stronger?",
             "Yes — enter the weaker leg's number for the more useful, "
             "honest tier, and consider extra single-leg volume on that "
             "side until the gap closes."),
        ],
    },
}


ORDER = [
    "pull-up", "dip", "push-up", "bench-press", "squat", "deadlift",
    "chin-up", "overhead-press", "muscle-up", "pistol-squat", "ring-dip",
    "weighted-pull-up", "l-sit", "handstand-push-up",
    "bulgarian-split-squat",
]
