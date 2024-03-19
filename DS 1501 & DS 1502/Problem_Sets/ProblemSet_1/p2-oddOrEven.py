num = int(input())
if(num % 2 == 0 & num > 0):{
    print("The number is even")
}
elif(num%2 == 1 & num > 0):{
    print("The number is odd")
}
elif(num == 0):{
    print("The number is zero")
}
else:{
    print("Please enter a valid number")
}