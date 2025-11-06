#!/usr/bin/env python3
"""
Universal Agentic Setup - Quick Start Script
One-command installation for Claude Code and/or GitHub Copilot agents.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


class AgenticQuickStart:
    """Quick start installer for Agentic Setup Framework."""

    def __init__(self):
        self.repo_path = Path.cwd()
        self.setup_dir = Path(__file__).parent.resolve()
        self.claude_script = self.setup_dir / "agentic_setup/claude-code/scripts/implement_framework.py"
        self.copilot_apm_script = self.setup_dir / "agentic_setup/github-copilot/scripts/install_apm.py"
        self.copilot_analyze_script = self.setup_dir / "agentic_setup/github-copilot/scripts/analyze_project.py"
        self.copilot_setup_script = self.setup_dir / "agentic_setup/github-copilot/scripts/setup_copilot_agents.py"

    def show_banner(self):
        """Display welcome banner."""
        print("""
╔══════════════════════════════════════════════════════════╗
║       🤖  UNIVERSAL AGENTIC SETUP - QUICK START  🤖       ║
║                                                          ║
║    Transform your AI coding assistants into             ║
║    intelligent multi-agent systems                      ║
╚══════════════════════════════════════════════════════════╝
        """)

    def detect_environment(self) -> Tuple[bool, bool, bool]:
        """Detect available tools and environments."""
        has_vscode = os.path.exists("/Applications/Visual Studio Code.app") or \
                     os.path.exists(os.path.expanduser("~/.vscode")) or \
                     os.path.exists("/usr/bin/code")

        has_node = subprocess.run(["which", "node"], capture_output=True).returncode == 0
        has_git = subprocess.run(["which", "git"], capture_output=True).returncode == 0

        return has_vscode, has_node, has_git

    def select_platform(self) -> str:
        """Let user select which platform to install."""
        print("\n📦 Select Installation Type:")
        print("=" * 50)

        has_vscode, has_node, has_git = self.detect_environment()

        print("\n🔍 Environment Detection:")
        print(f"   VS Code:  {'✅ Found' if has_vscode else '❌ Not found'}")
        print(f"   Node.js:  {'✅ Found' if has_node else '❌ Not found'}")
        print(f"   Git:      {'✅ Found' if has_git else '✅ Found'}")

        print("\n🎯 Available Options:")
        print("   1. Claude Code       - CLI-based, deep analysis")
        print("   2. GitHub Copilot    - VS Code, real-time guidance")
        print("   3. Both              - Maximum quality control")
        print("   4. APM Only          - Copilot with full APM workflow")
        print("   5. Exit")

        while True:
            choice = input("\n👉 Enter your choice [1-5]: ").strip()

            if choice == "1":
                return "claude"
            elif choice == "2":
                return "copilot"
            elif choice == "3":
                return "both"
            elif choice == "4":
                return "apm"
            elif choice == "5":
                print("\n👋 Goodbye!")
                sys.exit(0)
            else:
                print("❌ Invalid choice. Please enter 1-5.")

    def install_claude(self):
        """Install Claude Code setup."""
        print("\n🟣 Installing Claude Code Setup...")
        print("-" * 50)

        if not self.claude_script.exists():
            print(f"❌ Script not found: {self.claude_script}")
            return False

        try:
            result = subprocess.run(
                [sys.executable, str(self.claude_script), str(self.repo_path)],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("✅ Claude Code setup complete!")
                return True
            else:
                print(f"❌ Installation failed: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ Error: {e}")
            return False

    def install_copilot_traditional(self):
        """Install traditional Copilot setup."""
        print("\n🟢 Installing GitHub Copilot Setup (Traditional)...")
        print("-" * 50)

        # Run analyzer
        print("📊 Analyzing project...")
        try:
            result = subprocess.run(
                [sys.executable, str(self.copilot_analyze_script), str(self.repo_path)],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print(f"❌ Analysis failed: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ Error during analysis: {e}")
            return False

        # Run setup
        print("⚙️  Installing configuration...")
        try:
            result = subprocess.run(
                [sys.executable, str(self.copilot_setup_script), str(self.repo_path)],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print("✅ GitHub Copilot setup complete!")
                return True
            else:
                print(f"❌ Setup failed: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ Error during setup: {e}")
            return False

    def install_copilot_apm(self):
        """Install Copilot with APM."""
        print("\n🚀 Installing GitHub Copilot with APM...")
        print("-" * 50)

        if not self.copilot_apm_script.exists():
            print(f"❌ Script not found: {self.copilot_apm_script}")
            return False

        try:
            result = subprocess.run(
                [sys.executable, str(self.copilot_apm_script), str(self.repo_path)],
                capture_output=True,
                text=True
            )

            print(result.stdout)

            if result.returncode == 0:
                print("✅ GitHub Copilot APM setup complete!")
                return True
            else:
                print(f"❌ Installation failed: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ Error: {e}")
            return False

    def run(self):
        """Execute the quick start installation."""
        self.show_banner()

        print(f"\n📍 Current Project: {self.repo_path}")
        print(f"📁 Setup Location: {self.setup_dir}")

        platform = self.select_platform()

        success = True

        if platform == "claude":
            success = self.install_claude()

        elif platform == "copilot":
            # Ask if they want APM
            print("\n💡 APM (Agentic Project Management) provides:")
            print("   - Test-driven development workflow")
            print("   - Copilot Chat modes (plan/implement/review)")
            print("   - GitHub issue integration")
            print("   - Automated testing and verification")

            use_apm = input("\n🎯 Use APM setup? [Y/n]: ").strip().lower()

            if use_apm != 'n':
                success = self.install_copilot_apm()
            else:
                success = self.install_copilot_traditional()

        elif platform == "both":
            claude_ok = self.install_claude()

            # Ask about APM for Copilot
            print("\n💡 For GitHub Copilot, use APM setup? [Y/n]: ")
            use_apm = input("👉 ").strip().lower()

            if use_apm != 'n':
                copilot_ok = self.install_copilot_apm()
            else:
                copilot_ok = self.install_copilot_traditional()

            success = claude_ok and copilot_ok

        elif platform == "apm":
            success = self.install_copilot_apm()

        # Final message
        print("\n" + "=" * 60)
        if success:
            print("✨ Installation Complete!")
            print("\n📚 Next Steps:")

            if platform in ["claude", "both"]:
                print("\n🟣 Claude Code:")
                print("   1. Make code changes")
                print("   2. Commit with: git commit")
                print("   3. Agents will review automatically")
                print("   4. Use /review for manual agent review")

            if platform in ["copilot", "both", "apm"]:
                print("\n🟢 GitHub Copilot:")
                print("   1. Open VS Code")
                print("   2. Open Copilot Chat")

                if platform == "apm" or (platform in ["copilot", "both"] and use_apm != 'n'):
                    print("   3. Use APM commands:")
                    print("      - /repo-assess   - Analyze codebase")
                    print("      - /apm-plan      - Plan features")
                    print("      - /apm-implement - Write code")
                    print("      - /apm-verify    - Test & verify")
                else:
                    print("   3. Paste master prompt from .github/copilot/prompts.md")
                    print("   4. Start coding with multi-agent guidance!")

            print("\n📖 Documentation:")
            print(f"   {self.setup_dir}/README.md")

        else:
            print("⚠️  Installation had some issues.")
            print("Please check the error messages above.")
            print("\n💡 For help, see:")
            print(f"   {self.setup_dir}/README.md")


def main():
    """CLI entry point."""
    quickstart = AgenticQuickStart()

    try:
        quickstart.run()
    except KeyboardInterrupt:
        print("\n\n👋 Installation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()