import sys
import pickle as p #序列化
import os

diao = os.path.exists('D:\diao.dat')

class xuliehua:
    def chuangjian(self):
        if os.path.exists('diao') == False:
            f = open('diao', 'wb')
            temp = {'total': 0}
            p.dump(temp, f)
            f.close()
            print("\n本地磁盘尚无通讯录，新通讯录创建成功！\n")
        else:
            pass

class PhoneBook:

    record_list =[]
    record_id = 0  #类变量，id的初始值，每个记录的id，

    def __init__(self,name=''): #初始化个name，让此类中下面的方法也可用
        self.name = name

    def input_record(self):#输入方法
        name = input('请输入姓名:') #输入的数值赋给name
        phone_number = input('请输入电话:') #输入的数值赋给phone
        record = {'name':name,'phone_number':phone_number} #构造出记录
        return record  #完事把字典结果返回

    def add_record(self):#添加方法
        record = self.input_record() #调用input_record,获取name和phone构成记录
        global record_id  #声明此id就是函数外的id，每次调用全局的都会+1
        PhoneBook.record_id += 1 #构成记录后为该记录记上id
        record['record_id'] = self.record_id  #将record_id的数值赋给字典里的record_id
        self.record_list.append(record)   #将记录加入到列表中，append添加到末尾
        return '添加成功'  #添加完毕后，返回添加成功

    def query_record(self):#查询方法，通过姓名来查询
        query_result = []   #保存查询结果
        query_ids =[]   #保存查询id
        for record in self.record_list: #让字典去list通讯录中查询
            if record['name'] == self.name: #1.如果该字典中的nama=要查询的name
                query_result.append(record) #2.那么把查询到的结果放入到query_result
                query_ids.append(record['record_id'])   #3.把record_id加入到query_ids中
        return query_ids,query_result   #返回字典和字典中id的数值

    def delete_record(self):#删除方法
        query_ids,query_result = self.query_record(self)    #查询函数寻找ids和所有记录的列表
        if len(query_ids) == 0: #使用长度判断
            print('此人不存在')
        else:
            if len(query_result) > 1:   #查询出同样的保存结果大于1，进行for循环，将字典的每一个记录都打印出来
                for record in query_result:
                    print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
                record_id = input("请输入要删除的id")  #将重复的id删除
                if int(record_id) in query_ids:     #校验输入的id是否在列表里
                    for record in self.record_list:
                        if int(record_id) == record['record_id']:
                            self.record_list.remove(record)
                else:
                    print('输入错误')
            else:
                print("{}\t{}\t{}".format(query_result[0]["record_id"], query_result[0]["name"], query_result[0]["phone_number"]))
                while True:
                    s = input('是否确认删除(Y/N):')
                    if s in ['Y','N']:
                        if s == 'Y':
                            self.record_list(query_result[0])
                        else:
                            pass
                        break
                    else:
                        print('输入错误')

    def change_record(self):#修改方法
        query_ids, query_result = self.query_record(self)
        if len(query_ids) == 0:
            print("不存在!!!")
        else:
            if len(query_result) > 1:
                for record in query_result:
                    print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
                record_id = input("请选择要修改的id:")
                if int(record_id) in query_ids:
                    for record in self.record_list:
                        if int(record_id) == record["record_id"]:
                            phone_number = input("请输入修改后的电话号码:")
                            record["phone_number"] = phone_number
                            print("修改成功")
                            break
                else:
                    print("输入错误!!!")
            else:
                print("{}\t{}\t{}".format(query_result[0]["record_id"],query_result[0]["name"], query_result[0]["phone_number"]))
                phone_number = input("请输入修改后的电话号码:")
                query_result[0]["phone_number"] = phone_number
                print("修改成功")

    def tuichu():#退出方法
        print('谢谢使用')
        sys.exit()

if __name__ == "__main__":
    while True:
        menu = """
               通讯录
               1. 添加
               2. 查找
               3. 删除
               4. 修改
               5. 退出
               """
        print(menu)
        s = input("请选择操作:")
        if s in ["1", "2", "3", "4", "5"]:
            if s == '1':
                msg = PhoneBook().add_record()
                print(msg)
                continue

            if s == '2':
                name = input('请输入姓名:')
                query_ids, query_result = PhoneBook(name).query_record()
                if len(query_ids) == 0:
                    print("不存在")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone_number"]))
                        continue
            if s == '3':
                name = input('请输入姓名')
                PhoneBook(name).delete_record()
                continue
            if s == '4':
                name = input('请输入姓名')
                PhoneBook(name).change_record()
                continue
            if s =='5':
                PhoneBook().tuichu()
            else:
                print('输入错误')
                continue

