#!/usr/bin/env python3
"""
Simple test script for the Model agent.
"""

from agent import check_server, calculate, read_file, write_file, get_time, list_files, MODEL, LOCAL, PORT


def test_server_connection():
    """Test if the server is running."""
    print("Testing server connection...")
    if check_server():
        print("✅ Server is running")
        return True
    else:
        print("❌ Server is not running")
        print(f"Make sure your AI Navigator server is running on {LOCAL}:{PORT}")
        return False


def test_tools():
    """Test the available tools."""
    print("\nTesting tools...")

    # Test calculation
    print("Testing calculator...")
    result = calculate("2 + 3 * 4")
    print(f"  {result}")

    # Test time
    print("Testing time...")
    result = get_time()
    print(f"  {result}")

    # Test file listing
    print("Testing file listing...")
    result = list_files(".")
    print(f"  {result}")

    # Test file write
    print("Testing file write...")
    result = write_file("test_output.txt", "Hello from Model agent test!")
    print(f"  {result}")

    # Test file read
    print("Testing file read...")
    result = read_file("test_output.txt")
    print(f"  {result}")


def main():
    """Main test function."""
    print("🧪 Model Agent Test")
    print("=" * 30)
    print(f"API URL: {LOCAL}:{PORT}")
    print(f"Model: {MODEL}")
    print()

    # Test server connection
    server_ok = test_server_connection()

    # Test tools
    test_tools()

    if server_ok:
        print("\n✅ All tests completed successfully!")
        print("You can now run: python agent.py")
    else:
        print("\n⚠️  Server tests failed, but tool tests passed.")
        print("Start your AI Navigator server and try again.")


if __name__ == "__main__":
    main()
