from PIL import Image
import os

def convert_masks(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            filepath = os.path.join(directory, filename)
            image = Image.open(filepath).convert("RGBA")  # 强制转换为RGBA模式
            image_data = image.load()
            width, height = image.size
            
            for y in range(height):
                for x in range(width):
                    r, g, b, _ = image_data[x, y]  # RGBA模式下有四个值
                    if r == 0 and g == 0 and b == 0:  # 黑色mask
                        image_data[x, y] = (128, 0, 0, 255)  # 转换为红色
                    elif r == 128 and g == 0 and b == 0:  # 红色mask
                        image_data[x, y] = (0, 0, 0, 255)  # 转换为黑色
                    # elif r == 0 and g == 128 and b == 0:  # 绿色mask
                    #     image_data[x, y] = (128, 0, 0, 255)  # 转换为红色
            
            image.save("/Users/zhangyuchen/Desktop/Results Fig/xxformer/" + filename)

# 使用示例
directory_path = "/Users/zhangyuchen/Desktop/Results Fig/xxformer"
convert_masks(directory_path)
print("done")