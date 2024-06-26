import json

def code100(points,count):
    for point in points:
        x,y = point[0],point[1]

        c1=(x-250)**2+(y-150)**2
        c2=(x-410)**2+(y-150)**2

        if (x>=145 and x<=165 and y>=75 and y<=225) or (c1<=75**2 and c1>=55**2) or (c2<=75**2 and c2>=55**2):
            count+=1
    
    return count
        
        
if __name__=='__main__':
    
    json_data=open('code_100.json','r')
    data_points=json.load(json_data)
    points=data_points['coords']
    count=0
    
    result=code100(points,count)
    print(result)