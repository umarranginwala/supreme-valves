// Product Categories and Data for Supreme Valves India
const productCategories = {
    "ball-valves": {
        name: "Ball Valves",
        icon: "fa-circle-dot",
        description: "Quarter-turn valves for on/off control",
        products: [
            { name: "Ball Valve", url: "products/ball-valve.html", tags: ["general", "multi-purpose"] },
            { name: "NAB Ball Valve Screwed End Full Port", url: "products/nab-ball-valve-screwed-end-full-port.html", tags: ["marine", "fire-safe", "bronze"] },
            { name: "Three Piece Ball Valve", url: "products/three-piece-ball-valve.html", tags: ["maintenance-friendly"] },
            { name: "Two Piece Ball Valve", url: "products/two-piece-ball-valve.html", tags: ["compact"] },
            { name: "Single Piece Ball Valve", url: "products/single-piece-ball-valve.html", tags: ["economical"] },
            { name: "Three Way Ball Valve", url: "products/three-way-ball-valve.html", tags: ["diverting", "mixing"] },
            { name: "IC Ball Valve 1PC Screw End", url: "products/ic-ball-valve-1pc-screw-end.html", tags: ["threaded"] },
            { name: "IC Ball Valve 1PC Flange End", url: "products/ic-ball-valve-1pc-flange-end.html", tags: ["flanged"] },
            { name: "IC Ball Valve 2PC Flange End", url: "products/ic-ball-valve-2pc-flange-end.html", tags: ["flanged"] },
            { name: "IC Ball Valve 3PC Screw End", url: "products/ic-ball-valve-3pc-screw-end.html", tags: ["threaded"] },
            { name: "IC Ball Valve 3PC Flange End 150", url: "products/ic-ball-valve-3pc-flange-end-150.html", tags: ["class-150"] },
            { name: "IC Ball Valve 3PC Flange End 300", url: "products/ic-ball-valve-3pc-flange-end-300.html", tags: ["class-300"] },
            { name: "CS Ball Valve 3PC Flange End", url: "products/cs-ball-valve-3pc-flange-end.html", tags: ["carbon-steel"] },
            { name: "CI Ball Valve 2PC Flange End", url: "products/ci-ball-valve-2pc-flange-end.html", tags: ["cast-iron"] },
            { name: "CI Ball Valve 3PC Flange End", url: "products/ci-ball-valve-3pc-flange-end.html", tags: ["cast-iron"] },
            { name: "Ball Valve with Actuator", url: "products/ball-valve-actuator.html", tags: ["automated", "actuated"] },
            { name: "Fire Safe Ball Valve", url: "products/fire-safe-ball-valve.html", tags: ["fire-protection", "api-607"] },
            { name: "Cryogenic Ball Valve", url: "products/cryogenic-ball-valve.html", tags: ["low-temperature", "lng"] },
            { name: "Trunnion Mounted Ball Valve", url: "products/trunnion-mounted-ball-valve.html", tags: ["high-pressure"] },
            { name: "Forged Steel Ball Valve", url: "products/forged-steel-ball-valve.html", tags: ["high-pressure", "forged"] },
            { name: "PTFE Lined Ball Valve", url: "products/ptfe-lined-ball-valve.html", tags: ["corrosion-resistant", "chemical"] },
            { name: "Jacketed Ball Valve", url: "products/jacketed-ball-valve-flange-end.html", tags: ["temperature-control"] },
            { name: "PP Ball Valve Flange End", url: "products/pp-ball-valve-flange-end.html", tags: ["polypropylene", "chemical"] },
            { name: "IC Flush Bottom Ball Valve", url: "products/ic-flush-bottom-ball-valve.html", tags: ["tank-bottom"] },
            { name: "IC TC End Ball Valve", url: "products/ic-tc-end-ball-valve.html", tags: ["tri-clamp", "sanitary"] },
            { name: "IC Three Way Ball Valve Screw End", url: "products/ic-three-way-ball-valve-screw-end.html", tags: ["three-way"] },
            { name: "Three Way Ball Valve Flange End", url: "products/three-way-ball-valve-flange-end.html", tags: ["three-way"] },
            { name: "CI MS SS Ball Valve 1PC Screw End", url: "products/ci-ms-ss-ball-valve-1pc-screw-end.html", tags: ["multi-material"] }
        ]
    },
    "gate-valves": {
        name: "Gate Valves",
        icon: "fa-bars",
        description: "Linear motion valves for full flow",
        products: [
            { name: "Gate Valve", url: "products/gate-valve.html", tags: ["general", "full-bore"] },
            { name: "Gate Valve Flange End 150", url: "products/gate-valve-flange-end-150.html", tags: ["class-150", "flanged"] },
            { name: "Knife Gate Valve", url: "products/knife-gate-valve.html", tags: ["slurry", "wastewater"] },
            { name: "Knife Edge Gate Valve", url: "products/knife-edge-gate-valve.html", tags: ["slurry"] },
            { name: "Knife Edge Gate Valve Flanged", url: "products/knife-edge-gate-valve-flanged.html", tags: ["slurry", "flanged"] },
            { name: "Pressure Seal Gate Valve", url: "products/pressure-seal-gate-valve.html", tags: ["high-pressure"] },
            { name: "CI Gate Valve Flange End", url: "products/ci-gate-valve-flange-end.html", tags: ["cast-iron"] },
            { name: "SS Gate Valve Flange End", url: "products/ss-gate-valve-flange-end.html", tags: ["stainless-steel"] },
            { name: "IC Gate Valve Screw End", url: "products/ic-gate-valve-screw-end.html", tags: ["threaded"] },
            { name: "Forged Steel Gate Globe Valve", url: "products/forged-steel-gate-globe-valve.html", tags: ["forged", "high-pressure"] }
        ]
    },
    "globe-valves": {
        name: "Globe Valves",
        icon: "fa-globe",
        description: "Throttling and flow control valves",
        products: [
            { name: "Globe Valve", url: "products/globe-valve.html", tags: ["general", "throttling"] },
            { name: "Globe Valve Flange End 150", url: "products/globe-valve-flange-end-150.html", tags: ["class-150", "flanged"] },
            { name: "Pressure Seal Globe Valve", url: "products/pressure-seal-globe-valve.html", tags: ["high-pressure"] },
            { name: "CI Globe Valve Flange End", url: "products/ci-globe-valve-flange-end.html", tags: ["cast-iron"] },
            { name: "SS Globe Valve Flange End", url: "products/ss-globe-valve-flange-end.html", tags: ["stainless-steel"] },
            { name: "IC Globe Valve Screw End", url: "products/ic-globe-valve-screw-end.html", tags: ["threaded"] }
        ]
    },
    "check-valves": {
        name: "Check Valves",
        icon: "fa-arrow-right",
        description: "Non-return and backflow prevention",
        products: [
            { name: "Check Valve", url: "products/check-valve.html", tags: ["general", "non-return"] },
            { name: "NRV Horizontal & Vertical Type", url: "products/nrv-horizontal-vertical-type.html", tags: ["fire-protection", "ss-304"] },
            { name: "Swing Check Valve", url: "products/swing-check-valve.html", tags: ["swing-type"] },
            { name: "Lift Check Valve", url: "products/lift-check-valve.html", tags: ["lift-type"] },
            { name: "Wafer Check Valve", url: "products/wafer-check-valve.html", tags: ["wafer-type", "space-saving"] },
            { name: "Dual Plate Check Valve", url: "products/dual-plate-check-valve.html", tags: ["dual-plate", "compact"] },
            { name: "Non-Slam Check Valve", url: "products/non-slam-check-valve.html", tags: ["silent", "no-slam"] },
            { name: "Swing Check Valve Flange End", url: "products/swing-check-valve-flange-end.html", tags: ["swing", "flanged"] },
            { name: "Wafer Check Valve Barstock", url: "products/wafer-check-valve-barstock.html", tags: ["wafer", "barstock"] },
            { name: "CI Check Valve Flange End", url: "products/ci-check-valve-flange-end.html", tags: ["cast-iron"] },
            { name: "SS Check Valve Flange End", url: "products/ss-check-valve-flange-end.html", tags: ["stainless-steel"] },
            { name: "IC Disc Check Valve", url: "products/ic-disc-check-valve.html", tags: ["disc-type"] },
            { name: "IC Wafer Check Valve", url: "products/ic-wafer-check-valve.html", tags: ["wafer"] },
            { name: "PP NRV Flange End", url: "products/pp-nrv-flange-end.html", tags: ["polypropylene"] },
            { name: "CI Foot Valve Flange End", url: "products/ci-foot-valve-flange-end.html", tags: ["foot-valve"] },
            { name: "PP Foot Valve Flange End", url: "products/pp-foot-valve-flange-end.html", tags: ["polypropylene", "foot-valve"] }
        ]
    },
    "butterfly-valves": {
        name: "Butterfly Valves",
        icon: "fa-circle-notch",
        description: "Quarter-turn disc valves for large diameter",
        products: [
            { name: "Butterfly Valve", url: "products/butterfly-valve.html", tags: ["general", "quarter-turn"] },
            { name: "Butterfly Valve PN10", url: "products/butterfly-valve-pn10.html", tags: ["pn10"] },
            { name: "Butterfly Valve PN16", url: "products/butterfly-valve-pn16.html", tags: ["pn16"] },
            { name: "SS904L Butterfly Valve Pneumatic", url: "products/ss904l-butterfly-valve-pneumatic.html", tags: ["ss904l", "pneumatic", "corrosion-resistant"] },
            { name: "Triple Offset Butterfly Valve 10 Inch", url: "products/triple-offset-butterfly-valve-10inch.html", tags: ["triple-offset", "high-performance"] },
            { name: "NAB Butterfly Valve DN150 Lug", url: "products/nab-butterfly-valve-dn150-lug.html", tags: ["nab", "marine"] },
            { name: "NAB Butterfly Valve DN100", url: "products/nab-butterfly-valve-dn100.html", tags: ["nab", "marine"] },
            { name: "NAB Butterfly Valve DN80 Lug", url: "products/nab-butterfly-valve-dn80-lug.html", tags: ["nab", "marine"] },
            { name: "PTFE Lined Butterfly Valve", url: "products/ptfe-lined-butterfly-valve.html", tags: ["ptfe-lined", "chemical"] }
        ]
    },
    "control-valves": {
        name: "Control Valves",
        icon: "fa-sliders",
        description: "Automated flow and pressure control",
        products: [
            { name: "Control Valve", url: "products/control-valve.html", tags: ["general", "automated"] },
            { name: "Motorized Control Valve", url: "products/motorized-control-valve.html", tags: ["electric", "motorized"] },
            { name: "Control Valve Electric", url: "products/control-valve-electric.html", tags: ["electric"] },
            { name: "Control Valve Pneumatic", url: "products/control-valve-pneumatic.html", tags: ["pneumatic"] }
        ]
    },
    "safety-valves": {
        name: "Safety & Relief Valves",
        icon: "fa-shield-halved",
        description: "Pressure protection and relief",
        products: [
            { name: "Safety Relief Valve", url: "products/safety-relief-valve.html", tags: ["safety", "overpressure"] },
            { name: "Pressure Safety Valve", url: "products/pressure-safety-valve.html", tags: ["safety", "asme"] },
            { name: "Pressure Reducing Valve", url: "products/pressure-reducing-valve.html", tags: ["pressure-control"] }
        ]
    },
    "strainers": {
        name: "Strainers & Filters",
        icon: "fa-filter",
        description: "Pipeline filtration and protection",
        products: [
            { name: "Strainers", url: "products/strainers.html", tags: ["general", "filtration"] },
            { name: "Brass Y-Type Strainer BSP", url: "products/brass-y-type-strainer-bsp.html", tags: ["brass", "y-type", "fire-protection"] },
            { name: "Y-Type Strainer", url: "products/y-type-strainer.html", tags: ["y-type"] },
            { name: "Basket Strainer", url: "products/basket-strainer.html", tags: ["basket-type"] },
            { name: "Basket Strainer Flange End", url: "products/basket-strainer-flange-end.html", tags: ["basket", "flanged"] },
            { name: "Duplex Strainer", url: "products/duplex-strainer.html", tags: ["duplex", "continuous-operation"] },
            { name: "IC Y-Strainer Flange End", url: "products/ic-y-strainer-flange-end.html", tags: ["y-type", "flanged"] },
            { name: "IC Y-Strainer Screw End", url: "products/ic-y-strainer-screw-end.html", tags: ["y-type", "threaded"] },
            { name: "CI Y-Strainer Flange End", url: "products/ci-y-strainer-flange-end.html", tags: ["cast-iron"] },
            { name: "CI Y-Strainer Screw End", url: "products/ci-y-strainer-screw-end.html", tags: ["cast-iron"] },
            { name: "CS Y-Strainer Flange End", url: "products/cs-y-strainer-flange-end.html", tags: ["carbon-steel"] }
        ]
    },
    "specialty-valves": {
        name: "Specialty Valves",
        icon: "fa-star",
        description: "Specialized applications and custom solutions",
        products: [
            { name: "Plug Valve", url: "products/plug-valve.html", tags: ["quarter-turn"] },
            { name: "Plug Valve Lubricated", url: "products/plug-valve-lubricated.html", tags: ["lubricated"] },
            { name: "Needle Valve", url: "products/needle-valve.html", tags: ["precision", "throttling"] },
            { name: "Diaphragm Valve", url: "products/diaphragm-valve.html", tags: ["corrosive", "slurry"] },
            { name: "Diaphragm Valve Weir Type", url: "products/diaphragm-valve-weir-type.html", tags: ["weir-type"] },
            { name: "Diaphragm Valve Straight Through", url: "products/diaphragm-valve-straight-through.html", tags: ["straight-through"] },
            { name: "Piston Valve", url: "products/piston-valve.html", tags: ["high-pressure"] },
            { name: "Pinch Valve Sleeve Type", url: "products/pinch-valve-sleeve-type.html", tags: ["pinch", "slurry"] },
            { name: "Blow Down Valve", url: "products/blow-down-valve.html", tags: ["boiler", "blowdown"] },
            { name: "Flush Bottom Valve", url: "products/flush-bottom-valve.html", tags: ["tank-bottom"] },
            { name: "Custom Valve", url: "products/custom-valve.html", tags: ["custom", "engineered"] }
        ]
    },
    "steam-traps": {
        name: "Steam Traps & Accessories",
        icon: "fa-fire",
        description: "Steam system components",
        products: [
            { name: "Steam Trap Thermodynamic", url: "products/steam-trap-thermodynamic.html", tags: ["thermodynamic", "steam"] },
            { name: "IC Steam Trap Thermodynamic", url: "products/ic-steam-trap-thermodynamic.html", tags: ["thermodynamic"] },
            { name: "CI Bucket Float Steam Trap", url: "products/ci-bucket-float-steam-trap.html", tags: ["bucket-float"] },
            { name: "Moisture Separator", url: "products/moisture-separator.html", tags: ["steam", "separator"] },
            { name: "Sight Glass", url: "products/sight-glass.html", tags: ["visual-indication"] },
            { name: "IC Full View Sight Glass", url: "products/ic-full-view-sight-glass.html", tags: ["sight-glass"] },
            { name: "IC Double Window Sight Glass", url: "products/ic-double-window-sight-glass.html", tags: ["sight-glass"] },
            { name: "Full View Sight Glass Barstock", url: "products/full-view-sight-glass-barstock.html", tags: ["sight-glass"] },
            { name: "Gauge Glass Cock Set", url: "products/gauge-glass-cock-set.html", tags: ["gauge-glass"] }
        ]
    }
};

// All products flattened for search
const allProducts = [];
Object.keys(productCategories).forEach(categoryKey => {
    const category = productCategories[categoryKey];
    category.products.forEach(product => {
        allProducts.push({
            ...product,
            category: category.name,
            categoryKey: categoryKey,
            categoryIcon: category.icon
        });
    });
});

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { productCategories, allProducts };
}
