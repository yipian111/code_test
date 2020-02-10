# -*- coding:utf-8 -*-


def fastsort(arr, left, right):
    '''
    快速排序
    (1)首先设定一个分界值，通过该分界值将数组分成左右两部分。 [2] 
    (2)将大于或等于分界值的数据集中到数组右边，小于分界值的数据集中到数组的左边。此时，左边部分中各元素都小于或等于分界值，而右边部分中各元素都大于或等于分界值。 [2] 
    (3)然后，左边和右边的数据可以独立排序。对于左侧的数组数据，又可以取一个分界值，将该部分数据分成左右两部分，同样在左边放置较小值，右边放置较大值。右侧的数组数据也可以做类似处理。 [2] 
    (4)重复上述过程，可以看出，这是一个递归定义。通过递归将左侧部分排好序后，再递归排好右侧部分的顺序。当左、右两个部分各数据排序完成后，整个数组的排序也就完成了。
    '''
    if left >= right:
        return
    
    i = left
    j = right
    flag = i  # 默认标记为元素0
    # i 从前往后，大于标记则交换，j从后往前，小于标记则交换
    while i < j:
        while j > i:
            if arr[j] < arr[flag] and j>flag:
                temp = arr[flag]
                arr[flag] = arr[j]
                arr[j] = temp

                flag = j
            else:
                j = j - 1

        while i < j:
            if arr[i] > arr[flag] and i<flag:
                temp = arr[flag]
                arr[flag] = arr[i]
                arr[i] = temp

                flag = i
            else:
                i = i + 1

    if i > 1:
        fastsort(arr, 0, i - 1)
    if j < right:
        fastsort(arr, j + 1, right)
    

if __name__ == '__main__':
    a = [9, 4, 5, 66, 7, 6, 44, 8, 12, 12, 189, 90, 0, 33]
    print(a)
    fastsort(a, 0, len(a) - 1)
    print(a)
