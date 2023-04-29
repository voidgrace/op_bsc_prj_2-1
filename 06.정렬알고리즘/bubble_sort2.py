from typing import MutableSequence

def bubble_sort(a:MutableSequence)->None:

    n=len(a)
    for i in range(n-1):
        exchng=0
        for j in range(n-1,i,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                exchng+=1
        if exchng==0 :
            break

    for i in range(n-1):
        print(f'패스 {i+1}')
        for j in range(n-1,i,-1):
            for m in range(0,n-1):
                print(f'{a[m]:2}'+(' ' if m!= j-1 else
                                   '+' if a[j-1]>a[j]else' -'),
                                    end='')
            print(f'{a[n-1]:2}')
if __name__ =='__main__':
    print('버블 정렬을 수행합니다.')
    num=int(input('원소 수를 입력하세요.'))
    x=[None]*num

    for i in range(num):
        x[i]=int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}]={x[i]}')