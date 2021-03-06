#将成绩数据先全部列出，然后遍历循环，同时在进行排序。最后插入科目表和平均成绩
with open("report.txt","r",encoding="gbk") as f:
    all_data = f.readlines() #all_data 文件所有信息

student_total = len(all_data[1:]) #学生人数
student_data = all_data[1:] #student_data  #学生成绩数据
subject =all_data[0].split() #subject #考试主题
subject_count = len(subject[1:]) #subject_count #需要考试的数量
subject.insert(0, "名次")  # 插入名次
all_list = []  #存放新数据的列表
list_score = []

#计算学生成绩总和与平均值，替换60以下的数据为“不合格”
for student in student_data: #遍历截取出的学生成绩
    sum = 0          # sum 单个学生的成绩总分
    student_info=student.split() #student_info 学生成绩信息
    list_score.append(student_info[1:])  # 添加除名字外的成绩
    for fraction in student_info[1:]: #遍历除名字外的分数
        sum += int(fraction)     #叠加求和
    new_student_info= ["不及格" if eval(x) < 60 else x for x in student_info[1:]] #替换分数
    new_student_info.insert(0, student_info[0]) #插入对应名字
    new_student_info.append(sum) #添加每个学生的成绩总分
    average = int(sum / subject_count) #平均分
    new_student_info.append("%.2f" % average) #添加平均分并保留其2位小数
    all_list.append(new_student_info) #将学生信息加入总列表
grades_ranking = sorted(all_list, key=lambda x: x[-2], reverse=True) #对学生总分从大到小进行倒叙，生成一个新的列表，保障原信息不发生改变

#求出学生每门平均分和每人总分
average_score=["平均"] #需要添加的所有学生每科考试的平均分列表
all_score = 0 #负责记录全体学生的总分数
for number in range(subject_count): #设置一个可以使内循环遍历到我想要该位元素的外循环
    reccord = 0 #记录相同位置分数的起始，也负责清零
    for site in list_score:#遍历包含全体学生分数列表的学生成绩列表
        reccord  += int(site[number]) #将所有被遍历列表相同位置元素整数化进行叠加
    score = "%.f"%(reccord / student_total) #score(该科目分数）将所有学生改科目得分总和出学生总分数（student_tatol)
    average_score.append(score) #添加到总平均分数列表，当循环一次添加一次
    all_score += reccord #all_score(总分）将每个课的成绩进行叠加
avg =all_score / student_total # 总分/总学生人数
avg_standard = avg / subject_count #每个学生的总平均分 / 总课数
average_score.append(round(avg))
average_score.append(round(avg_standard))

#将信息写入一个文件，
with open("test_two.txt","w+",encoding="gbk") as w:
    all_list.insert(0, subject) #在all_list(总遍历列表）插入考试科目名
    for Subject_name in all_list[0]: #遍历新插入的科目
        w.write("%s\t" % Subject_name) #将遍历的课程，写入文件
    w.write("\n") #完成遍历后，写入一个换行符
#遍历已排序的成绩列表，根据已排名的列表位置来插入序号
    grades_ranking.insert(0,average_score) #将总平均插入到排名榜中
    for e in grades_ranking:  #遍历成绩列表
        e.insert(0, grades_ranking.index(e)) #在遍历的列表前插入该元素在总列表中的位置
        for t in e: #遍历成绩列表
            w.write("%s\t"%(t)) #依次写入被遍历的列表元素，并在元素后加入一个制表符
        w.write("\n") #列表读取完后，写入一个换行符
