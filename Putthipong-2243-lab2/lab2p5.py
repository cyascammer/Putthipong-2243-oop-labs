'''
Puttthipong Phukhansung
633040224-3
'''

taekwondo_olympics2020_w49k = {
    "Gold": {"Thailand"}
}

taekwondo_olympics2020_w49k.update ({        
    "Silver": {"Spain"},
    "Bronze": {"Israel", "Serbia"},
})

def F():
    for key, value in taekwondo_olympics2020_w49k.items():
        for x in value:
            print(x, "received",key,"medal")

if __name__ == '__main__':
    F()
    print("The dictionary of medals is", taekwondo_olympics2020_w49k)