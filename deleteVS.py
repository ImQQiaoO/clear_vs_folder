import os
import shutil
import time


def delete_vs_folder_in_current_directory(directory):
    # 构造当前目录中的.vs文件夹的完整路径
    vs_folder = os.path.join(directory, ".vs")
    # 检查.vs文件夹是否存在
    if os.path.exists(vs_folder):
        # 删除.vs文件夹
        shutil.rmtree(vs_folder)
        print(f"Deleted {vs_folder}")


def get_old_subfolders(directory, days_):
    # 获取当前时间
    current_time = time.time()
    threshold_time = current_time - (days_ * 24 * 60 * 60)

    # 获取指定目录下的所有文件和文件夹
    all_items = os.listdir(directory)
    old_subfolders = [
        item for item in all_items
        if os.path.isdir(os.path.join(directory, item)) and os.path.getmtime(
            os.path.join(directory, item)) < threshold_time
    ]

    return old_subfolders


if __name__ == '__main__':
    days = input("要删除多少天内无编辑的项目的.vs文件夹：")
    file_list = get_old_subfolders('.', int(days))
    print(f"以下是{days}天内无修改记录的文件夹：")
    for i in file_list:
        print(i)
    confirm = input("确认删除以上目录中的.vs文件夹请按y")
    if confirm == 'y' or confirm == 'Y':
        for i in file_list:
            delete_vs_folder_in_current_directory(i)
