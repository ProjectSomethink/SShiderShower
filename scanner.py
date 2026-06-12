import os

# Your specific system targets
SYSTEM_KEYWORDS = ["osiris", "exloader"]
# Your full list of cheat names for browser detection
BROWSER_KEYWORDS = [
    "osiris", "exloader", "nixware", "memesense", "xone", "interium", 
    "skinchanger", "extrimhack", "sharkhack", "fecurity", "aimstar", 
    "iniuria", "legendware", "weave", "aimmy", "cs2.glow", "hvh"
]

def scan_files():
    found_items = []
    # 1. SYSTEM SCAN (Strict: Osiris & Exloader only)
    # Scans your user profile/documents
    base_path = os.environ.get('USERPROFILE', '')
    for root, dirs, files in os.walk(base_path):
        # Skip browser/system folders to keep this list strictly focused
        if any(ign in root.lower() for ign in ['mozilla', 'firefox', '.nuget', 'steam', 'windows']):
            continue
            
        for name in dirs + files:
            name_lower = name.lower()
            if any(k in name_lower for k in SYSTEM_KEYWORDS):
                if not name_lower.endswith(('.xml', '.xsd', '.vdf', '.png', '.lnk')):
                    found_items.append(os.path.abspath(os.path.join(root, name)))
    return list(set(found_items))

def scan_browser_data():
    browser_found = []
    roaming = os.environ.get('APPDATA', '')
    firefox_path = os.path.join(roaming, 'Mozilla\\Firefox\\Profiles')
    
    if os.path.exists(firefox_path):
        for root, dirs, files in os.walk(firefox_path):
            # 2. BROWSER SCAN (Broad: All cheat names)
            if 'storage' in root or 'cache' in root:
                for cheat in BROWSER_KEYWORDS:
                    if cheat in root.lower():
                        browser_found.append(os.path.abspath(root))
                        break 
    return list(set(browser_found))