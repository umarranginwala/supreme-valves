#!/usr/bin/env python3
"""
Add comprehensive technical specifications to all product pages
Based on the brochure data provided
"""

import json
import re
from pathlib import Path

# Technical specifications data from brochure
TECHNICAL_SPECS = {
    # IC Ball Valves
    "ic-ball-valve-1pc-screw-end": {
        "design_std": "BS 5351",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As Per ANSI B 16.10",
        "end_connection": "Screw: BSP / BSPT / NPT Female Threading",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["1/4\"", "3/8\"", "1/2\"", "3/4\"", "1\"", "1.1/4\"", "1.1/2\"", "2\"", "2.1/2\"", "3\"", "4\""],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT",
            "Gland Packing": "PTFE/GFT"
        },
        "features": [
            "Positive Sealing",
            "No Steam Leakage",
            "Quarter Turn Operation",
            "Bubble Tight Shut-Off",
            "Self Cleaning PTFE seats offer long life and low torque"
        ]
    },
    "ic-ball-valve-1pc-flange-end": {
        "design_std": "BS 5351",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As Per ANSI B 16.10",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["3/4\"", "1\"", "1.1/2\"", "2\"", "2.1/2\"", "3\"", "4\""],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT",
            "Stem Seal": "PTFE/GFT"
        }
    },
    "ic-ball-valve-2pc-flange-end": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["15mm", "20mm", "25mm", "40mm", "50mm", "65mm", "80mm", "100mm", "125mm", "150mm"],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M/WCB",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT",
            "Stem Seal": "PTFE/GFT"
        }
    },
    "ic-ball-valve-3pc-screw-end": {
        "design_std": "BS 5351 / API 602",
        "testing_std": "API 598 / BS 5146",
        "end_connection": "BSP / NPT / Socket Weld",
        "socket_weld": "ANSI B 16.11",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["1/2\"", "3/4\"", "1\"", "1.1/4\"", "1.1/2\"", "2\"", "2.1/2\"", "3\""],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT",
            "Stem Seal": "PTFE/GFT"
        },
        "notes": [
            "Above 2\" valves have round body design, below that square body design",
            "65mm and above lever material will be MS"
        ]
    },
    "ic-ball-valve-3pc-flange-end-150": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["15mm", "20mm", "25mm", "32mm", "40mm", "50mm", "65mm", "80mm", "100mm", "125mm", "150mm", "200mm", "250mm"],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT",
            "Stem Seal": "PTFE/GFT"
        },
        "features": [
            "Also available in Gear Operated & Actuator Operated Design",
            "Above 2\" valves have round body design, below that square body design"
        ]
    },
    "ic-ball-valve-3pc-flange-end-300": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "300",
        "body_test": "1100 PSI",
        "seat_test": "800 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["25mm", "40mm", "50mm", "65mm", "80mm", "100mm"],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT"
        }
    },
    "cs-ball-valve-3pc-flange-end": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class_150": {
            "body_test": "425 PSI",
            "seat_test": "300 PSI",
            "max_temp": "180°C"
        },
        "pressure_class_300": {
            "body_test": "1100 PSI",
            "seat_test": "800 PSI",
            "max_temp": "180°C"
        },
        "air_test": "80 PSI",
        "sizes": ["1/2\"", "3/4\"", "1\"", "1.1/4\"", "1.1/2\"", "2\"", "2.1/2\"", "3\"", "4\"", "5\"", "6\"", "8\"", "10\""],
        "materials": {
            "Body": "C.S. (ASTM A 216 Gr. WCB)",
            "Ball": "S.S. 202/304/316",
            "Stem": "S.S. 202/304/316",
            "Seat Ring": "PTFE/GFT"
        },
        "features": [
            "Fire safe and Antistatic design available on request",
            "10\" valve will have gear operation",
            "12\" valve also available on request"
        ]
    },
    "ci-ball-valve-3pc-flange-end": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "215 PSI",
        "seat_test": "145 PSI",
        "max_temp": "180°C",
        "sizes": ["1/2\"", "3/4\"", "1\"", "1 1/4\"", "1 1/2\"", "2\"", "2 1/2\"", "3\"", "4\"", "6\"", "8\""],
        "materials": {
            "Body": "C.I.",
            "Ball": "S.S. 202/304/316",
            "Stem": "S.S. 202/304/316",
            "Seat Ring": "PTFE"
        },
        "notes": [
            "Square body design - upto 3\", Round body design - 4\" & above",
            "'E' / 'F' table also available"
        ]
    },
    "ci-ball-valve-2pc-flange-end": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "215 PSI",
        "seat_test": "145 PSI",
        "max_temp": "180°C",
        "sizes": ["1\"", "1.1/2\"", "2\"", "2.1/2\"", "3\"", "4\""],
        "materials": {
            "Body": "C.I.",
            "Ball": "SS 202/304/316",
            "Stem": "SS 202/304/316",
            "Seat Ring": "PTFE"
        },
        "features": [
            "Also available with locking lever"
        ]
    },
    "ci-ms-ss-ball-valve-1pc-screw-end": {
        "design_std": "BS 5351",
        "testing_std": "API 598",
        "face_to_face": "As per ANSI B 16.10",
        "end_connection": "Screw BSP / NPT",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["1/4\"", "3/8\"", "1/2\"", "3/4\"", "1\"", "1.1/4\"", "1.1/2\"", "2\"", "2.1/2\"", "3\"", "4\""],
        "materials": {
            "Body": "M.S./C.I./S.S. 202/304/316",
            "Ball": "S.S. 202/304/316",
            "Stem": "S.S. 202/304/316",
            "Seat Ring": "PTFE/GFT"
        }
    },
    "forged-steel-ball-valve": {
        "design_std": "BS 5351 / API 602",
        "testing_std": "API 598 / BS 5146",
        "end_connection": "Screw: BSP / NPT / Socket Weld / Reduce Bore",
        "pressure_class": "800",
        "body_test": "1100 PSI",
        "seat_test": "800 PSI",
        "max_temp": "180°C",
        "sizes": ["1/2\"", "3/4\"", "1\"", "1.1/2\"", "2\""],
        "materials": {
            "Body": "ASTM A-105, A-182 (F 304 & F 316)",
            "Ball": "AISI 304, 316",
            "Stem": "AISI 304, 316",
            "Seat Ring": "PTFE/GFT"
        },
        "features": [
            "Socket weld also available",
            "Full bore valves also available"
        ]
    },
    "ic-three-way-ball-valve-screw-end": {
        "design_std": "BS 5351 / API 602",
        "testing_std": "API 598 / BS 5146",
        "end_connection": "BSP / NPT",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["1/2\"", "3/4\"", "1\"", "1.1/2\"", "2\""],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT"
        },
        "features": [
            "Available in 'T' Port & 'L' Port Ball Design"
        ]
    },
    "three-way-ball-valve-flange-end": {
        "design_std": "BS 5351 / API 602",
        "testing_std": "API 598 / BS 5146",
        "end_connection": "Flange End 150#",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["15mm", "20mm", "25mm", "32mm", "40mm", "50mm", "65mm", "80mm", "100mm", "125mm", "150mm"],
        "materials": {
            "Body": "WCB (C.S.)/M.S./S.S. 202/304/316",
            "Ball": "AISI 304/AISI 316/S.S. 202",
            "Stem": "AISI 304/AISI 316/S.S. 202",
            "Seat Ring": "PTFE/GFT"
        },
        "features": [
            "Available in 'T' Port & 'L' Port Ball Design"
        ]
    },
    "ic-flush-bottom-ball-valve": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["25x40mm", "40x50mm", "50x80mm", "80x100mm"],
        "materials": {
            "Body": "ASTM A 351 Gr. CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 202/304/316/304L/316L",
            "Seat Ring": "PTFE/GFT"
        },
        "features": [
            "45° Lever Operation also available",
            "90° lever operation also available"
        ]
    },
    "jacketed-ball-valve-flange-end": {
        "design_std": "Low Operating Torque, Leak Tight Stem Sealing",
        "pressure_rating": "150#",
        "end_connection": "Flange End RF",
        "flange_drilling": "As per ANSI B 16.5, 150#",
        "face_to_face": "As per ANSI B16.10",
        "operation": "Manual Hand Lever Operated",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["25x40mm", "40x50mm", "50x65mm", "50x80mm", "65x80mm", "80x100mm", "100x150mm"],
        "materials": {
            "Body": "M.S./S.S. 304/S.S. 316",
            "Ball": "AISI 304/316",
            "Stem": "AISI 304/316",
            "Ball Seat": "PTFE/GFT/CFT",
            "Jacket": "M.S./SS304/SS316"
        }
    },
    "ic-tc-end-ball-valve": {
        "design_std": "BS 5351",
        "testing_std": "API 598 / BS 5146",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "180°C",
        "air_test": "80 PSI",
        "sizes": ["15MM", "20MM", "25MM", "40MM", "50MM"],
        "materials": {
            "Body": "ASTM A351 GR CF8/CF8M/CF3/CF3M",
            "Ball": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L",
            "Seat Ring": "PTFE/GFT"
        }
    },
    "butterfly-valve-pn10": {
        "design_std": "API 609 / IS: 13095",
        "testing_std": "API 598 / IS 13095",
        "temp_rating": "Material will be selected according to service",
        "pressure_class": "PN 10",
        "body_test": "15 Bar",
        "seat_test": "10 Bar",
        "temp_range": "60°C - 200°C",
        "sizes": ["1 1/2\"", "2\"", "2 1/2\"", "3\"", "4\"", "5\"", "6\"", "8\"", "10\"", "12\""],
        "materials": {
            "Body": "C.I./C.S./S.S. 202/S.S. 304/S.S. 316",
            "Disc": "C.I./D.I./S.G. Iron/C.S./CF8/CF8M",
            "Spindle": "AISI 410/S.S. 304/S.S. 316",
            "Rubber Lining": "Nitrile/EPDM/Viton/Silicon"
        },
        "features": [
            "Butterfly range available upto 28\"",
            "Gear Operated also available"
        ]
    },
    "butterfly-valve-pn16": {
        "design_std": "API 609 / IS: 13095",
        "testing_std": "API 598 / IS 13095",
        "temp_rating": "Material will be selected according to service",
        "pressure_class": "PN 16",
        "body_test": "22 Bar",
        "seat_test": "16 Bar",
        "temp_range": "60°C - 200°C",
        "sizes": ["1 1/2\"", "2\"", "2 1/2\"", "3\"", "4\"", "5\"", "6\"", "8\"", "10\"", "12\"", "14\"", "16\""],
        "materials": {
            "Body": "Cast Iron/Cast Steel/S.S. 304-316",
            "Disc": "Cast Iron/Cast Steel/S.S. 304-316",
            "Spindle": "S.S. 410/304/316",
            "Body Lining": "Nitrile/EPDM/Silicon/Viton/Hypalon"
        },
        "features": [
            "ISO 5211 mounting",
            "Butterfly range available upto 28\"",
            "Gear Operated also available"
        ]
    },
    "ptfe-lined-ball-valve": {
        "sizes": ["1\"", "1.1/2\"", "2\"", "3\"", "4\""],
        "materials": {
            "Body": "SG Iron, WCB or S.S.",
            "Ball": "PFA/FEP Lined MS or S.S.",
            "Stem": "Lined M.S. or S.S.",
            "Seat Ring": "PTFE"
        },
        "features": [
            "For corrosive media applications",
            "PFA/FEP lining options"
        ]
    },
    "ptfe-lined-butterfly-valve": {
        "design_std": "API 609",
        "drilling_std": "Universal",
        "max_temp_fep": "160°C",
        "max_temp_pfa": "160°C",
        "sizes": ["50mm", "65mm", "80mm", "100mm", "125mm", "150mm", "200mm", "250mm", "300mm", "350mm"],
        "materials": {
            "Body Liner": "PTFE/FEP/PFA 3mm Thick",
            "Disc": "AISI 304/316/FEP/PFA Lined",
            "Guide Bush": "S.S. AISI 304"
        },
        "features": [
            "Butterfly range available upto 28\"",
            "For corrosive and aggressive media"
        ]
    },
    "gate-valve-flange-end-150": {
        "design_std": "ANSI B 16.34 / API 600",
        "testing_std": "API 598",
        "face_to_face": "As per ANSI B 16.10",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "300°C",
        "air_test": "80 PSI",
        "sizes": ["25mm", "40mm", "50mm", "65mm", "80mm", "100mm", "125mm", "150mm", "200mm", "250mm", "300mm"],
        "materials": {
            "Body": "CF8/CF8M/C.I./C.S.",
            "Bonnet": "CF8/CF8M/C.I./C.S.",
            "Wedge": "CF8/CF8M/AISI 410 (13%CR)",
            "Seat Ring": "CF8/CF8M/AISI 410 (13%CR)",
            "Stem": "CF8/CF8M/AISI 410 (13%CR)"
        }
    },
    "globe-valve-flange-end-150": {
        "design_std": "BS 5351 / API 6D",
        "testing_std": "API 598 / BS 5146",
        "face_to_face": "As per ANSI B 16.11",
        "end_connection": "Flange as per ANSI B 16.5",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "300°C",
        "air_test": "80 PSI",
        "sizes": ["25mm", "40mm", "50mm", "65mm", "80mm", "100mm", "125mm", "150mm", "200mm", "250mm", "300mm"],
        "materials": {
            "Body": "CF8/CF8M/C.I./C.S.",
            "Bonnet": "CF8/CF8M/C.I./C.S.",
            "Seat Ring": "CF8/CF8M/C.I./C.S.",
            "Globe": "CF8/CF8M/AISI 410 (13%CR)",
            "Stem": "CF8/CF8M/AISI 410 (13%CR)"
        }
    },
    "ic-gate-valve-screw-end": {
        "design_std": "ANSI B 16.34 / API 600",
        "testing_std": "API 598",
        "face_to_face": "As per ANSI B 16.10",
        "end_connection": "Screw - BSP/NPT",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "300°C",
        "air_test": "80 PSI",
        "sizes": ["1/2\"", "3/4\"", "1\"", "1.1/2\"", "2\""],
        "materials": {
            "Body": "ASTM A351 GR. CF8/CF8M/CF3/CF3M",
            "Bonnet": "ASTM A351 GR. CF8/CF8M/CF3/CF3M",
            "Wedge": "ASTM A351 GR. CF8/CF8M/CF3/CF3M",
            "Stem": "AISI 304/316/304L/316L"
        }
    },
    "ic-globe-valve-screw-end": {
        "design_std": "ANSI B 16.34 / API 600",
        "testing_std": "API 598",
        "face_to_face": "As per ANSI B 16.10",
        "end_connection": "Screw - BSP/NPT",
        "pressure_class": "150",
        "body_test": "425 PSI",
        "seat_test": "300 PSI",
        "max_temp": "300°C",
        "air_test": "80 PSI",
        "sizes": ["1/2\"", "3/4\"", "1\"", "1.1/2\"", "2\""],
        "materials": {
            "Body": "ASTM A351 GR. CF8/CF8M/CF3/CF3M",
            "Bonnet": "ASTM A351 GR. CF8/CF8M/CF3/CF3M",
            "Globe": "AISI 304/316/304L/316L",
            "Stem": "AISI 304/316/304L/316L"
        }
    },
    "forged-steel-gate-globe-valve": {
        "design_std": "BS 5352 / API 602",
        "testing_std": "BS 6755 (Part-1) / API 598",
        "face_to_face": "As per ANSI B 16.10",
        "end_connection": "Screw End to BSP/NPT",
        "pressure_class_800": {
            "body_test": "3000 PSIG",
            "back_seat_test": "2000 PSIG",
            "seat_test": "2000 PSIG",
            "pneumatic_test": "80 PSIG"
        },
        "pressure_class_1500": {
            "body_test": "5400 PSIG",
            "back_seat_test": "4000 PSIG",
            "seat_test": "4000 PSIG",
            "pneumatic_test": "80 PSIG"
        },
        "sizes": ["1/2\"", "3/4\"", "1\"", "1.1/2\"", "2\""],
        "materials": {
            "Body": "ASTM A 105/F11/F12/F22/F304/F316",
            "Bonnet": "ASTM A 105/F11/F12/F22/F304/F316",
            "Disc": "AISI 410/304/316",
            "Seat Ring": "AISI 410/304/316",
            "Spindle": "AISI 410/304/316"
        }
    },
    "needle-valve": {
        "design_std": "As per Mfr's Std.",
        "testing_std": "BS5146",
        "end_connection": "Screwed BSP",
        "round_body_test": "1000 PSI",
        "square_body_test": "3000 PSI",
        "sizes": ["1/4\" - 3/8\"", "1/2\"", "3/4\"", "1\"", "1.1/2\"", "2\""],
        "materials": {
            "Body": "S.S. 202/S.S. 304/S.S. 316",
            "Bonnet": "S.S. 202/S.S. 304/S.S. 316",
            "Stem": "S.S. 202/S.S. 304/S.S. 316",
            "Gland Packing": "PTFE"
        },
        "features": [
            "6000 PSI and 10000 PSI available on request"
        ]
    }
}

print("Technical specifications data structure created.")
print(f"Total products with specs: {len(TECHNICAL_SPECS)}")
