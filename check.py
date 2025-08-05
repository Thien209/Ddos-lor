import os
import time

def quet_co_ban():
    appdata = os.getenv("APPDATA")
    minecraft_mods = os.path.join(appdata, ".minecraft", "mods")
    hack_keywords = ["meteor", "thunder", "wurst", "impact", "sigma", "future", "jigsaw", "forgehax", "aristois"]

    print("\n[!] Đang quét thư mục mods/ ...\n")
    time.sleep(1)
    if not os.path.exists(minecraft_mods):
        print("❌ Không tìm thấy thư mục mods.")
        return

    found = []
    for file in os.listdir(minecraft_mods):
        for keyword in hack_keywords:
            if keyword.lower() in file.lower():
                found.append(file)
                break

    if found:
        print("⚠️ Phát hiện client cheat:")
        for f in found:
            print(" -", f)
    else:
        print("✅ Không phát hiện client hack nào trong mods.")

def quet_chuyen_sau():
    appdata = os.getenv("APPDATA")
    paths_to_scan = [
        os.path.join(appdata, "meteor-client"),
        os.path.join(appdata, "thunder-client"),
        os.path.join(appdata, ".minecraft", "mods"),
        os.path.join(appdata, ".minecraft", "config"),
        os.path.join(appdata, ".minecraft", "versions")
    ]
    hack_keywords = ["meteor", "thunder", "wurst", "impact", "sigma", "future", "jigsaw", "forgehax", "aristois"]

    print("\n[!] Đang quét toàn diện...\n")
    time.sleep(1)

    found = []
    for path in paths_to_scan:
        if os.path.exists(path):
            for file in os.listdir(path):
                for keyword in hack_keywords:
                    if keyword.lower() in file.lower():
                        found.append(f"{file} (tại {path})")
                        break

    if found:
        print("⚠️ Phát hiện client cheat:")
        for f in found:
            print(" -", f)
    else:
        print("✅ Không phát hiện gì trong chế độ chuyên sâu.")

def main():
    print("=== CÁI NÀY ĐƯỢC MADE 100% TỪ BOT ===\n")
    print("Author: chatgpt - ý Tưởng : Lac13_09")
    print("Version: v1.0\n")
    print("╭────────────────────────────╮")
    print("│         Menu Quét          │")
    print("├────────────────────────────┤")
    print("│     1. Quét Sâu Vào File   │")
    print("│ 2. Quét Cơ Tầm chung mods  │")
    print("│   3. tắt                   │")
    print("╰────────────────────────────╯\n")

    lua_chon = input("Nhập  (1-3): ").strip()

    if lua_chon == "1":
        quet_chuyen_sau()
    elif lua_chon == "2":
        quet_co_ban()
    elif lua_chon == "3":
        print("👋 Tạm biệt!")
        return
    else:
        print("⚠️ Lựa chọn không hợp lệ!")

    input("\nNhấn Enter để thoát...")

if __name__ == "__main__":
    main()
