#-*- coding: utf-8 -*-

'''
@Author 최제현
@Date 21/1/8

'''

def main():
    filePath = './parsed.txt'
    try:
        file = open(filePath, 'r', encoding = 'utf-8')

    except:
        print('file open error!')
        exit(99)



if __name__ == '__main__':
    main()
