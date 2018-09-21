#include<iostream> 				//Program to find an element and print number of occurences and position of occurence
using namespace std;
int main()
{
	int f,n,i=0,j=0,a[20]={0},b[20]={0};
	cout<<"enter number of elements"<<endl;
	cin>>n;
	cout<<"enter array"<<endl;
	for(i=0;i<n;i++)
		{cin>>a[i];}
	cout<<"Enter element to be searched ";
	cin>>f;
	for(i=0;i<n;i++)
		if(f==a[i])
			{b[j]=i+1;
			j++;}
	cout<<"no of occurences of "<<f<<":"<<j;
	if(j!=0)
	{
		cout<<"\nposition(s) are "<<":";
		for(j=0;b[j]!=0;j++)
			cout<<b[j]<<" ";
		return 0;
	}
	
}
