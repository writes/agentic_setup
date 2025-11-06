#!/usr/bin/env python3
"""
Test script to verify the agentic setup installation is working.
"""

import os
import sys
from pathlib import Path


def test_structure():
    """Test that all required files and directories exist."""
    base_dir = Path(__file__).parent

    required_files = [
        "README.md",
        "quick_start.py",
        "agentic_setup/claude-code/README.md",
        "agentic_setup/claude-code/scripts/agent_detector.py",
        "agentic_setup/claude-code/scripts/implement_framework.py",
        "agentic_setup/claude-code/prompts/MASTER_CLAUDE_PROMPT.md",
        "agentic_setup/github-copilot/README.md",
        "agentic_setup/github-copilot/scripts/analyze_project.py",
        "agentic_setup/github-copilot/scripts/setup_copilot_agents.py",
        "agentic_setup/github-copilot/scripts/install_apm.py",
    ]

    print("🔍 Testing Agentic Setup Structure")
    print("=" * 50)

    all_good = True

    for file_path in required_files:
        full_path = base_dir / file_path
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ Missing: {file_path}")
            all_good = False

    print("=" * 50)

    if all_good:
        print("✨ All files present! Setup is ready to use.")
        print("\n📚 Quick Start:")
        print("   1. Navigate to your project: cd /path/to/project")
        print("   2. Run: python ~/agentic-setup/quick_start.py")
        print("   3. Follow the interactive prompts")
        return 0
    else:
        print("⚠️  Some files are missing. Please check your installation.")
        return 1


def test_imports():
    """Test that all Python scripts can be imported."""
    print("\n🧪 Testing Python Scripts")
    print("=" * 50)

    base_dir = Path(__file__).parent
    sys.path.insert(0, str(base_dir))

    scripts_to_test = [
        ("Claude Agent Detector", "agentic_setup.claude-code.scripts.agent_detector"),
        ("Claude Framework Installer", "agentic_setup.claude-code.scripts.implement_framework"),
        ("Copilot Analyzer", "agentic_setup.github-copilot.scripts.analyze_project"),
        ("Copilot Setup", "agentic_setup.github-copilot.scripts.setup_copilot_agents"),
        ("APM Installer", "agentic_setup.github-copilot.scripts.install_apm"),
    ]

    all_good = True

    for name, module_path in scripts_to_test:
        # Convert module path for file imports
        file_path = module_path.replace(".", "/") + ".py"
        full_path = base_dir / file_path

        if full_path.exists():
            # Check syntax by compiling
            try:
                with open(full_path) as f:
                    compile(f.read(), str(full_path), 'exec')
                print(f"✅ {name}")
            except SyntaxError as e:
                print(f"❌ {name}: Syntax error - {e}")
                all_good = False
        else:
            print(f"❌ {name}: File not found")
            all_good = False

    print("=" * 50)

    if all_good:
        print("✨ All scripts valid!")
        return 0
    else:
        print("⚠️  Some scripts have issues.")
        return 1


def main():
    """Run all tests."""
    print("""
╔══════════════════════════════════════════════════════════╗
║         🧪 AGENTIC SETUP - VERIFICATION TEST 🧪           ║
╚══════════════════════════════════════════════════════════╝
    """)

    # Test structure
    result1 = test_structure()

    # Test imports
    result2 = test_imports()

    # Summary
    print("\n📊 Test Summary")
    print("=" * 50)

    if result1 == 0 and result2 == 0:
        print("✅ All tests passed!")
        print("\n🎉 Your Agentic Setup is ready to use!")
        print("\n🚀 Get started:")
        print("   cd your-project")
        print("   python ~/agentic-setup/quick_start.py")
        return 0
    else:
        print("⚠️  Some tests failed. Please review the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())