#include <iostream>
#include <time.h>
using namespace std;

struct element{
element* next;
element* prev;
int number;
};
struct double_list{
element* head;
element* tail;
int counter;
};

void podzial(int x[],int n);
void pokaztab(int x[]);
void bubblemal(int x[],int n);
void bubbleros(int x[],int n);
void zad2(int x[]);
void add_tail(double_list &l,int value);
void add_head(double_list &l,int value);
void show(double_list l);
void zad3(double_list &l);
int main()
{
    srand(time(NULL));
    double_list l;
    l.counter=0;
    l.head=nullptr;
    l.tail=nullptr;

    int *tab=new int[10];
    for(int i=0;i<10;i++){
    int liczba=rand()%20+1;
    tab[i]=liczba;
    }
    cout<<"tablica przed podzialem\n"<<endl;
    pokaztab(tab);

    cout<<"\ntablica po podziale\n"<<endl;

    podzial(tab,10);

    pokaztab(tab);

    int *tab2=new int[10];
    for(int i=0;i<10;i++){
    int liczba1=rand()%20+1;
    tab2[i]=liczba1;
    }
    cout<<"\n"<<endl;
    zad3(l);

    zad2(tab);
    delete []tab;
    delete []tab2;
    return 0;
}

void podzial(int x[],int n){
int i=0;
int j=n-1;
while(i<j){
    while(x[i]<10&&i<j){
        i++;
    }
    while(x[j]>=10&&i<j){
        j--;
    }
    if(i<j){
        swap(x[i],x[j]);
        i++;
        j--;
    }
}
if(x[i]<10) cout<<"Jest tyle liczb jednocyfrowych: "<<i+2<<endl;
else cout<<i<<" Liczb jednocyfrowych"<<endl;
}

void pokaztab(int x[]){
for(int j=0;j<10;j++){
    cout<<x[j]<<" ";}
}

void bubbleros(int x[],int n){
    for(int i=n-1;i>0;i--){
            for(int j=5;j<i;j++){
                if(x[j]>x[j+1]) swap(x[j],x[j+1]);
            }

    }
}

void bubblemal(int x[],int n){
    for(int i=n-1;i>0;i--){
            for(int j=0;j<i;j++){
                if(x[j]<x[j+1]) swap(x[j],x[j+1]);
            }
    }
}
void zad2(int x[]){
    cout<<"\n Tablica przed sortowaniem\n"<<endl;
pokaztab(x);
bubbleros(x,5);
bubblemal(x,10);
cout<<"\nTablica po sortowaniu\n"<<endl;
pokaztab(x);
}
void add_tail(double_list &l,int value){
element*el=new element;
el->number=value;
el->next=nullptr;
el->prev=nullptr;
if(l.tail!=nullptr){
    l.tail->next=el;
    el->prev=l.tail;
}
else l.head=el;
l.tail=el;
l.counter++;
}

void add_head(double_list &l,int value){
element*el=new element;
el->number=value;
el->next=nullptr;
el->prev=nullptr;
if(l.head!=nullptr){
    l.head->prev=el;
    el->next=l.head;
}
else l.tail=el;
l.head=el;
l.counter++;
}

void show(double_list l){
element*temp=l.head;
for(int i=1;i<=l.counter;i++){
    cout<<temp->number<<" ";
    temp=temp->next;
}
}

void zad3(double_list &l){
    srand(time(NULL));
    for(int i=0;i<20;i++){
    int liczba1=rand()%20+1;
    if(liczba1%2==0) add_head(l,liczba1);
    else add_tail(l,liczba1);
    }
    cout<<"\nLista zad3\n"<<endl;
    show(l);
}
