#include<bits/stdc++.h>
int val=0;
static int count=0;
using std::cout;
using std::cin;
int main()
{
	std::string s,s1;
	std::getline(cin,s);
	std::vector<int> v,v1;

	for(int i=0;i<s.size();i+=2)
	{
		s1=s[i];
        val=std::stoi(s1);
		v.push_back(val);
	}
	int j=0;
	int t=v.size();
	while(t--)
	{
		for(int i=0;i<v.size();++i)
		{
			if((v[i]%v[j]==0 || v[j]%v[i]==0) && i!=j)
			{
				count++;
			}
		}
		j++;
		v1.push_back(count);
		count=0;
	}
	for(auto& x: v1)
	{
		cout<<x<<" ";
	}
}
