#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <tuple>
#include <map>

using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, pair<int,int>> dic;
    
    
    for (auto &s : records){
        stringstream ss(s);
        string token;
        vector<string> result;
        
        string time;
        int minute;
        string car;
        string inout;
        
        
        while (getline(ss, token, ' ')) // stringstream ss을 이용해 : 기준으로 split해 token에 저장
        {
            result.push_back(token);
        }
        
        time = result[0];
        car = result[1];
        inout = result[2];
        
        minute = stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 2));
        
        // cout << minute <<" " << car << " " << inout;
        
        
        if (dic.find(car) != dic.end()){
            if(inout == "IN")
            {
                dic[car].first = minute;
            }
            else{
                dic[car].second += (minute - dic[car].first);
                dic[car].first = -1;
            }
        }
        else{
            dic[car] = {minute, 0};
        }        
        
    }
    
    
    priority_queue<pair<string, int>, vector<pair<string, int>>, greater<pair<string, int>>> heap;


    for (auto &d : dic) {
        if (d.second.first != -1){
            d.second.second += (23 * 60 + 59) - d.second.first;
            d.second.first = -1;
        }
        
        int tmp = 0;
        cout << d.first << " " << d.second.first << " " << d.second.second << endl;
        if (d.second.second <= fees[0]){
            heap.push({d.first, fees[1]});
        } 
        else{
            d.second.second -= fees[0];
            tmp = fees[1];
            
            tmp += (ceil((double)d.second.second / fees[2])) * fees[3];
            heap.push({d.first, tmp});
        }
    }
    
   while (heap.empty() == false){
       auto [c, sums] = heap.top();
       heap.pop();
       
       answer.push_back(sums);
      
   }
    
    for (auto& a : answer){
        cout << a << endl;
    }
    
        
        
    return answer;
}