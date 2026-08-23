# -*- coding: utf-8 -*-
"""
Central config for all 15 Strength Standards Calculators.
Every page is generated from this file + templates/calculator.html,
so adding calculator #16 later just means adding a dict entry here.

Tier numbers are reasonable estimates assembled from the brief and
spot-checked against a couple of published strength-standards sites
(StrengthLevel-style bodyweight ratios, common calisthenics progression
charts). They are NOT authoritative — flagged again in README.md.
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
        ],
    },
}


ORDER = [
    "pull-up", "dip", "push-up", "bench-press", "squat", "deadlift",
    "chin-up", "overhead-press", "muscle-up", "pistol-squat", "ring-dip",
    "weighted-pull-up", "l-sit", "handstand-push-up",
    "bulgarian-split-squat",
]
