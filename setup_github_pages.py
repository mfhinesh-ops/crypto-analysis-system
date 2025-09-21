#!/usr/bin/env python3
"""
GitHub Pages Multi-Pillar Setup Script
Run this in your crypto-analysis-system repository root directory
"""

import os
import json
from datetime import datetime

def main():
    print("🚀 Setting up Crypto 1000x Analysis System GitHub Pages structure...")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('.git'):
        print("❌ Error: This doesn't appear to be a Git repository.")
        print("Please run this script from your crypto-analysis-system repository root.")
        return
    
    # Create the complete structure
    create_crypto_github_pages_structure()
    
    print("\n" + "=" * 60)
    print("🎉 Setup complete! Next steps:")
    print("1. git add .")
    print("2. git commit -m 'Add multi-pillar GitHub Pages structure'")
    print("3. git push origin main")
    print("4. Wait 2-3 minutes for GitHub Pages to build")
    print("\nYour URLs will be:")
    print("• Main: https://mfhinesh-ops.github.io/crypto-analysis-system/")
    print("• Adoption: https://mfhinesh-ops.github.io/crypto-analysis-system/adoption/")
    print("• Tokenomics: https://mfhinesh-ops.github.io/crypto-analysis-system/tokenomics/")

def create_crypto_github_pages_structure():
    """Create complete GitHub Pages structure for crypto 1000x analysis system"""
    
    # Define all pillars with their information
    pillars = {
        'adoption': {
            'weight': '15%', 
            'status': 'completed', 
            'desc': 'TVL, Users, Fees, Development, Integrations',
            'color': '#10B981',
            'icon': '✅'
        },
        'tokenomics': {
            'weight': '10%', 
            'status': 'in-progress', 
            'desc': 'Float Ratio, Unlocks, Holders, Revenue Multiple',
            'color': '#F59E0B',
            'icon': '🚧'
        },
        'team': {
            'weight': '15%', 
            'status': 'pending', 
            'desc': 'Experience, Track Record, Commitment',
            'color': '#6B7280',
            'icon': '⏳'
        },
        'investors': {
            'weight': '15%', 
            'status': 'pending', 
            'desc': 'Quality, Stage, Amount, Strategic Value',
            'color': '#6B7280',
            'icon': '⏳'
        },
        'market-relevance': {
            'weight': '10%', 
            'status': 'pending', 
            'desc': 'Market Size, Growth, Competition',
            'color': '#6B7280',
            'icon': '⏳'
        },
        'tech': {
            'weight': '15%', 
            'status': 'pending', 
            'desc': 'Innovation, Scalability, Architecture',
            'color': '#6B7280',
            'icon': '⏳'
        },
        'liquidity': {
            'weight': '8%', 
            'status': 'pending', 
            'desc': 'Volume, Spreads, Exchange Coverage',
            'color': '#6B7280',
            'icon': '⏳'
        },
        'security': {
            'weight': '5%', 
            'status': 'pending', 
            'desc': 'Audits, Bug Bounties, Track Record',
            'color': '#6B7280',
            'icon': '⏳'
        },
        'catalysts': {
            'weight': '4%', 
            'status': 'pending', 
            'desc': 'Upcoming Events, Partnerships, Releases',
            'color': '#6B7280',
            'icon': '⏳'
        },
        'regulatory': {
            'weight': '3%', 
            'status': 'pending', 
            'desc': 'Compliance, Risk Assessment, Jurisdiction',
            'color': '#6B7280',
            'icon': '⏳'
        }
    }
    
    # Create directory structure
    print("Creating directory structure...")
    
    # Create pillar directories
    for pillar in pillars.keys():
        os.makedirs(pillar, exist_ok=True)
        print(f"✅ Created {pillar}/ directory")
    
    # Create assets directory
    os.makedirs('assets/css', exist_ok=True)
    os.makedirs('assets/js', exist_ok=True)
    print("✅ Created assets/ directories")
    
    # Generate all files
    create_main_navigation(pillars)
    create_shared_css()
    create_shared_js()
    
    for pillar_name, pillar_data in pillars.items():
        create_pillar_page(pillar_name, pillar_data)
        create_pillar_data(pillar_name, pillar_data)

def create_main_navigation(pillars):
    """Create the main navigation hub (index.html)"""
    
    pillar_cards = ""
    for pillar_name, pillar_data in pillars.items():
        status_class = pillar_data['status'].replace('-', '_')
        btn_class = "btn" if pillar_data['status'] != 'pending' else "btn disabled"
        btn_text = "View Dashboard" if pillar_data['status'] != 'pending' else "Coming Soon"
        
        pillar_cards += f"""
            <div class="pillar-card {status_class}">
                <div class="pillar-header">
                    <h3>{pillar_name.replace('-', ' ').title()}</h3>
                    <span class="weight">{pillar_data['weight']}</span>
                </div>
                <p class="description">{pillar_data['desc']}</p>
                <div class="status" style="color: {pillar_data['color']}">{pillar_data['icon']} {pillar_data['status'].replace('-', ' ').title()}</div>
                <a href="{pillar_name}/" class="{btn_class}">{btn_text}</a>
            </div>"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto 1000x Analysis System</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>">
</head>
<body>
    <div class="container">
        <header class="main-header">
            <h1>🚀 Crypto 1000x Analysis System</h1>
            <p class="subtitle">Multi-Pillar Framework for Identifying 1000x Opportunities</p>
            <div class="last-updated">Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
        </header>
        
        <div class="system-overview">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value">42</div>
                    <div class="stat-label">Projects Analyzed</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">+0.419</div>
                    <div class="stat-label">Adoption Correlation</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">10</div>
                    <div class="stat-label">Analysis Pillars</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">1</div>
                    <div class="stat-label">Pillars Completed</div>
                </div>
            </div>
        </div>
        
        <section class="pillars-section">
            <h2>Analysis Pillars</h2>
            <div class="pillar-grid">{pillar_cards}
            </div>
        </section>
        
        <section class="methodology">
            <h2>Methodology</h2>
            <div class="methodology-grid">
                <div class="method-card">
                    <h3>📊 Statistical Validation</h3>
                    <p>Each pillar is validated against historical returns with correlation analysis and significance testing.</p>
                </div>
                <div class="method-card">
                    <h3>🔗 API-Driven</h3>
                    <p>Real-time data from CoinGecko, DeFiLlama, GitHub, and other authoritative sources.</p>
                </div>
                <div class="method-card">
                    <h3>⚖️ Weighted Scoring</h3>
                    <p>Each pillar contributes to the final score based on its proven predictive power.</p>
                </div>
                <div class="method-card">
                    <h3>🔍 Audit Trail</h3>
                    <p>Complete transparency with data sources, calculations, and decision rationale.</p>
                </div>
            </div>
        </section>
        
        <footer class="main-footer">
            <p>Built with ❤️ for the crypto community | Open source analysis framework</p>
            <div class="footer-links">
                <a href="https://github.com/mfhinesh-ops/crypto-analysis-system" target="_blank">GitHub Repository</a>
                <a href="adoption/">View Completed Analysis</a>
            </div>
        </footer>
    </div>
    
    <script src="assets/js/common.js"></script>
</body>
</html>"""
    
    with open("index.html", "w", encoding='utf-8') as f:
        f.write(html_content)
    print("✅ Created index.html (main navigation)")

def create_pillar_page(pillar_name, pillar_data):
    """Create individual pillar page"""
    
    status_section = ""
    if pillar_data['status'] == 'completed':
        status_section = """
        <div class="validation-results">
            <h2>Statistical Validation Results</h2>
            <div class="correlation-grid">
                <div class="correlation-card significant">
                    <div class="correlation-value">+0.419</div>
                    <div class="correlation-label">Adoption Overall</div>
                    <div class="correlation-status">✅ Significant</div>
                </div>
                <div class="correlation-card significant">
                    <div class="correlation-value">+0.511</div>
                    <div class="correlation-label">Development</div>
                    <div class="correlation-status">✅ Significant</div>
                </div>
                <div class="correlation-card">
                    <div class="correlation-value">+0.127</div>
                    <div class="correlation-label">Integration</div>
                    <div class="correlation-status">❌ Not Sig.</div>
                </div>
            </div>
            <p class="validation-note">Generated: 2025-09-19 22:23:03 | Sample Size: 42 | Critical Value (95%): ±0.310</p>
        </div>"""
    elif pillar_data['status'] == 'in-progress':
        status_section = """
        <div class="progress-section">
            <h2>Development Progress</h2>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 60%"></div>
            </div>
            <p>API integrations and scoring methodology in development...</p>
        </div>"""
    else:
        status_section = """
        <div class="pending-section">
            <h2>Coming Soon</h2>
            <p>This pillar is scheduled for development. Check back soon for updates!</p>
        </div>"""
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{pillar_name.replace('-', ' ').title()} Pillar - Crypto 1000x Analysis</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>">
</head>
<body>
    <div class="container">
        <nav class="breadcrumb">
            <a href="../" class="back-link">← Back to Main Dashboard</a>
        </nav>
        
        <header class="pillar-header">
            <h1>{pillar_data['icon']} {pillar_name.replace('-', ' ').title()} Pillar</h1>
            <div class="pillar-meta">
                <span class="weight">Weight: {pillar_data['weight']}</span>
                <span class="status {pillar_data['status']}" style="color: {pillar_data['color']}">
                    Status: {pillar_data['status'].replace('-', ' ').title()}
                </span>
            </div>
            <p class="pillar-description">{pillar_data['desc']}</p>
        </header>
        
        {status_section}
        
        <div class="pillar-content">
            <div id="{pillar_name}-dashboard">
                <div class="loading">Loading {pillar_name.replace('-', ' ').title()} data...</div>
            </div>
        </div>
        
        <div class="pillar-navigation">
            <h3>Other Pillars</h3>
            <div class="pillar-nav-grid">
                <a href="../adoption/" class="nav-pill {'active' if pillar_name == 'adoption' else ''}">Adoption (15%)</a>
                <a href="../tokenomics/" class="nav-pill {'active' if pillar_name == 'tokenomics' else ''}">Tokenomics (10%)</a>
                <a href="../team/" class="nav-pill {'active' if pillar_name == 'team' else ''}">Team (15%)</a>
                <a href="../investors/" class="nav-pill {'active' if pillar_name == 'investors' else ''}">Investors (15%)</a>
                <a href="../market-relevance/" class="nav-pill {'active' if pillar_name == 'market-relevance' else ''}">Market Relevance (10%)</a>
                <a href="../tech/" class="nav-pill {'active' if pillar_name == 'tech' else ''}">Tech (15%)</a>
                <a href="../liquidity/" class="nav-pill {'active' if pillar_name == 'liquidity' else ''}">Liquidity (8%)</a>
                <a href="../security/" class="nav-pill {'active' if pillar_name == 'security' else ''}">Security (5%)</a>
                <a href="../catalysts/" class="nav-pill {'active' if pillar_name == 'catalysts' else ''}">Catalysts (4%)</a>
                <a href="../regulatory/" class="nav-pill {'active' if pillar_name == 'regulatory' else ''}">Regulatory (3%)</a>
            </div>
        </div>
    </div>
    
    <script src="../assets/js/common.js"></script>
    <script>
        loadPillarData('{pillar_name}');
    </script>
</body>
</html>"""
    
    with open(f"{pillar_name}/index.html", "w", encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ Created {pillar_name}/index.html")

def create_pillar_data(pillar_name, pillar_data):
    """Create data.json for each pillar"""
    
    data = {
        "pillar_name": pillar_name,
        "weight": pillar_data['weight'],
        "status": pillar_data['status'],
        "description": pillar_data['desc'],
        "last_updated": datetime.now().isoformat(),
        "metrics": [],
        "projects": [],
        "validation": {
            "correlation": None,
            "p_value": None,
            "sample_size": 0,
            "significant": False
        }
    }
    
    if pillar_name == 'adoption':
        data["validation"] = {
            "correlation": 0.419,
            "p_value": 0.005,
            "sample_size": 42,
            "significant": True
        }
        data["metrics"] = [
            {"name": "TVL", "weight": 0.30, "correlation": 0.325},
            {"name": "Active Users", "weight": 0.20, "correlation": 0.267},
            {"name": "Transaction Fees", "weight": 0.20, "correlation": 0.189},
            {"name": "Developer Activity", "weight": 0.15, "correlation": 0.511},
            {"name": "Integrations", "weight": 0.15, "correlation": 0.127}
        ]
    
    with open(f"{pillar_name}/data.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Created {pillar_name}/data.json")

def create_shared_css():
    """Create shared CSS file"""
    css_content = """/* Crypto 1000x Analysis System - Shared Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 100%);
    color: #e2e8f0;
    line-height: 1.6;
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

.main-header {
    text-align: center;
    margin-bottom: 3rem;
}

.main-header h1 {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}

.subtitle {
    font-size: 1.25rem;
    color: #94a3b8;
    margin-bottom: 0.5rem;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}

.stat-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
}

.stat-value {
    font-size: 2rem;
    font-weight: 700;
    color: #10b981;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 0.875rem;
    color: #94a3b8;
}

.pillar-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.pillar-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 1.5rem;
    transition: all 0.3s ease;
}

.pillar-card:hover {
    transform: translateY(-4px);
}

.pillar-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.weight {
    background: rgba(255, 255, 255, 0.1);
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.875rem;
}

.description {
    color: #94a3b8;
    margin-bottom: 1rem;
    font-size: 0.875rem;
}

.btn {
    display: inline-block;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 500;
}

.btn.disabled {
    background: #374151;
    color: #9ca3af;
}

.breadcrumb {
    margin-bottom: 2rem;
}

.back-link {
    color: #94a3b8;
    text-decoration: none;
}

.pillar-header h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.validation-results {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 12px;
    padding: 2rem;
    margin-bottom: 2rem;
}

.correlation-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
}

.correlation-card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
}

.correlation-value {
    font-size: 1.5rem;
    font-weight: 700;
}

@media (max-width: 768px) {
    .main-header h1 { font-size: 2rem; }
    .pillar-grid { grid-template-columns: 1fr; }
}"""
    
    with open("assets/css/style.css", "w", encoding='utf-8') as f:
        f.write(css_content)
    print("✅ Created assets/css/style.css")

def create_shared_js():
    """Create shared JavaScript file"""
    js_content = """// Crypto 1000x Analysis System
async function loadPillarData(pillarName) {
    try {
        const response = await fetch('data.json');
        const data = await response.json();
        
        const loadingEl = document.querySelector('.loading');
        if (loadingEl) loadingEl.style.display = 'none';
        
        renderPillarDashboard(data);
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

function renderPillarDashboard(data) {
    const dashboardEl = document.querySelector(`#${data.pillar_name}-dashboard`);
    if (!dashboardEl) return;
    
    let content = '<div class="dashboard-content">';
    
    if (data.status === 'completed') {
        content += `<h3>Validation Results</h3>
                   <p>Correlation: ${data.validation.correlation}</p>
                   <p>Sample Size: ${data.validation.sample_size}</p>`;
    } else {
        content += `<p>Status: ${data.status}</p><p>${data.description}</p>`;
    }
    
    content += '</div>';
    dashboardEl.innerHTML = content;
}"""
    
    with open("assets/js/common.js", "w", encoding='utf-8') as f:
        f.write(js_content)
    print("✅ Created assets/js/common.js")

if __name__ == "__main__":
    main()
