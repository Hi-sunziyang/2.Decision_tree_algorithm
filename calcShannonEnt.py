from math import log


def create_dataset():
    dataset = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']  # 更改为离散值
    return dataset, labels


def calc_shannon_ent(dataset):
    num_entries = len(dataset)  # num_entries=5
    label_counts = {}  # 建立一个为了计算label频数的字典

    for line in dataset:  # 把dataset的每一行进行输入
        current_label = line[-1]  # -1指的是从最右边倒数第一列，current_labels=[['yes'],['yes'],['no'],['no'],['no']]
        if current_label not in label_counts.keys():
            label_counts[current_label] = 0
        label_counts[current_label] += 1

    print(label_counts)
    shannon_ent = 0.0

    for key in label_counts:
        prob = float(label_counts[key]) / num_entries  # 计算概率(频数/总数）
        shannon_ent -= prob * log(prob, 2)  # log base 2 #按照香农熵的公式计算
        print(f"{key}的概率是{prob}")  # 单个label的概率
    return shannon_ent


# 当数据集第（axis-1）个元素等于value时，去除第（axis-1）个元素，把剩下的元素整合成一个新的数据集
def split_dataset(dataset, axis, value):  # axis=0, value=1
    ret_dataset = []
    for line in dataset:
        if line[axis] == value:
            reduce_line = line[:axis]
            reduce_line.extend(line[axis + 1:])
            ret_dataset.append(reduce_line)
    return ret_dataset


my_dataset, my_labels = create_dataset()
print(my_dataset)

ShannonEnt = calc_shannon_ent(my_dataset)
print(f"香农熵={ShannonEnt}.")

my_second_dataset = split_dataset(my_dataset, 0, 1)  # 第一个元素是1的行拿出来，拿出来的行去除第一个元素
print(my_second_dataset)

my_third_dataset = split_dataset(my_dataset, 0, 0)  # 第一个元素是0的行拿出来，拿出来的行去除第一个元素
print(my_third_dataset)

my_fourth_dataset = split_dataset(my_dataset, 1, 1)  # 第二个元素是1的行拿出来，拿出来的行去除第二个元素
print(my_fourth_dataset)

my_fifth_dataset = split_dataset(my_dataset, 2, 'yes')  # 第三个元素是yes的行拿出来，拿出来的行去除第三个元素
print(my_fifth_dataset)

