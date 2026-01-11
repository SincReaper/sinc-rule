import os
import csv

# ================= 配置区域 =================
INPUT_FILE = 'chnroute.txt'       # 您的源文件名
OUTPUT_FILE = 'ikuai_import.csv'  # 生成的文件名
CHUNK_SIZE = 900                  # 每组 IP 数量 (保持 900 比较安全)
# ===========================================

def main():
    # 1. 定位文件路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, INPUT_FILE)
    output_path = os.path.join(script_dir, OUTPUT_FILE)

    if not os.path.exists(input_path):
        print(f"❌ 错误：找不到文件 {INPUT_FILE}")
        return

    print(f"正在读取 {INPUT_FILE} ...")

    try:
        # 2. 读取 IP 列表
        with open(input_path, 'r', encoding='utf-8-sig') as f:
            lines = [line.strip() for line in f if line.strip()]

        total_lines = len(lines)
        print(f"✅ 读取成功！共有 {total_lines} 个 IP。")

        # 3. 开始写入 CSV
        # newline='' 是为了防止 Windows 下出现空行
        with open(output_path, 'w', encoding='utf-8', newline='') as f_out:
            # 初始化 CSV 写入器
            writer = csv.writer(f_out)
            
            # 写入表头 (完全照搬您的 ipgroup.csv)
            # id, comment, type, group_name, addr_pool
            writer.writerow(['id', 'comment', 'type', 'group_name', 'addr_pool'])

            # 循环切分并写入
            group_count = 0
            for i in range(0, total_lines, CHUNK_SIZE):
                group_count += 1
                
                # 生成组名，例如: CN_Group_01
                group_name = f"CN_Group_{group_count:02d}"
                
                # 取出这一组的 IP
                chunk = lines[i : i + CHUNK_SIZE]
                
                # 把这一组几百个 IP 用逗号拼成一个长字符串
                addr_pool_str = ','.join(chunk)
                
                # 写入这一行
                # id 自动递增, comment 留空, type 填 0
                writer.writerow([group_count, '', 0, group_name, addr_pool_str])

        print("-" * 30)
        print(f"🎉 完美生成！文件路径：\n{output_path}")
        print(f"共生成了 {group_count} 个分组。")
        print("-" * 30)
        print("👉 现在请去爱快：【IP分组】->【导入】-> 选择这个 ikuai_import.csv")
        print("   这次一定能成功！")

    except Exception as e:
        print(f"❌ 发生错误：{e}")

if __name__ == '__main__':
    main()