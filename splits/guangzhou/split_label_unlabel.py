import os
import random
import shutil

# 定义train.txt文件路径和输出文件夹路径
train_txt_path = 'train.txt'
output_folder = r'F:\all_date\CD_Data_GZ\CD_GZ'
os.makedirs(output_folder, exist_ok=True)

# 读取train.txt中的图像名称
with open(train_txt_path, 'r') as file:
    image_names = file.read().splitlines()

# 定义要创建的不同比例的文件夹和比例
ratios = [5, 10, 20, 40]
for ratio in ratios:
    labeled_ratio = ratio
    unlabeled_ratio = 100 - ratio
    
    # 计算带标签和不带标签的数量
    total_images = len(image_names)
    num_labeled = total_images * labeled_ratio // 100
    num_unlabeled = total_images - num_labeled
    
    # 随机选择带标签的图像
    random.shuffle(image_names)
    labeled_image_names = image_names[:num_labeled]
    unlabeled_image_names = image_names[num_labeled:]
    
   # # 创建带标签和不带标签的文件夹
    labeled_folder = os.path.join(output_folder, f'{labeled_ratio}%', 'labeled')
    unlabeled_folder = os.path.join(output_folder, f'{labeled_ratio}%', 'unlabeled')
    os.makedirs(labeled_folder, exist_ok=True)
    os.makedirs(unlabeled_folder, exist_ok=True)
    
    # 复制带标签的图像到带标签的文件夹
   # for image_name in labeled_image_names:
   #     src_path = os.path.join(output_folder, image_name)
    #    dst_path = os.path.join(labeled_folder, image_name)
   #     shutil.copy(src_path, dst_path)
    
    # 复制不带标签的图像到不带标签的文件夹
  #  for image_name in unlabeled_image_names:
   #     src_path = os.path.join(output_folder, image_name)
   #     dst_path = os.path.join(unlabeled_folder, image_name)
   #     shutil.copy(src_path, dst_path)
    
    # 创建带标签和不带标签的txt文件并写入图像名称
    labeled_txt = os.path.join(output_folder, f'{labeled_ratio}%', 'labeled.txt')
    unlabeled_txt = os.path.join(output_folder, f'{labeled_ratio}%', 'unlabeled.txt')
    
    with open(labeled_txt, 'w') as file:
        file.write('\n'.join(labeled_image_names))
    
    with open(unlabeled_txt, 'w') as file:
        file.write('\n'.join(unlabeled_image_names))
    
    print(f"已创建 {labeled_ratio}% 的带标签文件夹和 {unlabeled_ratio}% 的不带标签文件夹")

print("分割完成")
