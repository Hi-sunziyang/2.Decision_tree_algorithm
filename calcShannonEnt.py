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


my_dataset, my_labels = create_dataset()
print(my_dataset)

ShannonEnt = calc_shannon_ent(my_dataset)
print(f"香农熵={ShannonEnt}.")
