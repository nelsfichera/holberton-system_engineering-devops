# 0x02. Dart - Classes 
## 📚Resources
- 🍎 [Dart Programming - Classes](https://www.tutorialspoint.com/dart_programming/dart_programming_classes.htm)
- 🍏 [Dart Inheritance](https://www.javatpoint.com/dart-inheritance#:~:text=Dart%20inheritance%20is%20defined%20as,Object%2DOriented%20programming%20approach)
- 🍎 [Null-aware Operators in Dart](https://medium.com/@thinkdigitalsoftware/null-aware-operators-in-dart-53ffb8ae80bb)
## 0. Welcome.
* Creating a User class:
* That contain propertie called name
and a method called showName that return string representation of User “Hello name”
```
youssef@Holberton/Dart$ cat 0-main.dart
import '0-class.dart';

void main() {
  final firstPer = User();
  firstPer.name = "Youssef Belhadj";
  print(firstPer.showName());
}
youssef@Holberton/Dart$ dart  0-main.dart
Hello Youssef Belhadj
youssef@Holberton/Dart$
```
## 1. User to Json
* Creating a User class:
    * Properties:
        * name : String
        * age : int
        * height: double
* With a method call toJson() that return a map representation of the User .
```
youssef@Holberton/Dart$ cat 1-main.dart
import '1-usertojson.dart';

void main() {
  final user = User(name: "Youssef", age: 25, height: 1.89);
print(user.toJson()));
}
youssef@Holberton/Dart$dart 1-main.dart
{name: Youssef, age: 25, height: 1.89}
youssef@Holberton/Dart$
```
## 2. Password
* Create a class called Password and give it a string property called password.
    * Add a method to Password calledisValid that returns true only
        * The length of password should be between 8 and 16.
        * password should contains Uppercase letters and lowercase letters
        * password should contains numbers .
        * toString :
            * Example password = "ShouldWorkf7ne"
            * Override the toString method of Password class to prints Your Password is: ShouldWorkf7ne.
```
youssef@Holberton/Dart$ cat 2-main.dart
import '2-password.dart';

void main() {
  final ps = Password();
  ps.password = "Just3z";
  if (ps.isValid() == true)
    print("${ps.password} is a Valid Password");
  else
    print("${ps.password} is Not a Valid Password");
  print("${ps.toString()}");
  ps.password = "ShouldWorkf7ne";
  if (ps.isValid() == true)
    print("${ps.password} is a Valid Password");
  else
    print("${ps.password} is Not a Valid Password");
  print("${ps.toString()}");
}

youssef@Holberton/Dart$dart 2-main.dart
Just3z is Not a Valid Password
Your Password is: Just3z
ShouldWorkf7ne is a Valid Password
Your Password is: ShouldWorkf7ne
youssef@Holberton/Dart$
```
## 3. Private Password
* Copy the last task and make the property password private
```
youssef@Holberton/Dart$ cat 3-main.dart
import '3-private_password.dart';

void main() {
  final ps = Password(password: "Passwordcode");
  print(ps.toString());
  print(ps.isValid());
  final ps2 = Password(password: "PasswordDecode3");
  print(ps2.toString());
  print(ps2.isValid());
}

youssef@Holberton/Dart$dart 3-main.dart
Your Password is Passwordcode
false
Your Password is PasswordDecode3
true
youssef@Holberton/Dart$
```
## 4. Mutables
* Lets make our data mutable now. Copy the code from the last task and add the Getters and Setters so we can assign and retrieve the value. * Should use get keyword for the getter. * Should use set keyword for the setter.
```
youssef@Holberton/Dart$ cat 4-main.dart
import '4-mutables.dart';
void main() {
  final password = Password(password: "Passwordecode");
  print(password.isValid());
  print(password.toString());
  password.password = "Youssef4321";
  print(password.isValid());
  print(password.toString());
}
youssef@Holberton/Dart$ dart 4-main.dart
Password Passwordecode
false
Password Youssef4321
true
youssef@Holberton/Dart$
```
## 5. Json to User
* Copy the code that you did in the 1-usertojson.dart add property called id to the User class
    * Add id to toJson() method
* Create a new instance called fromJson it accept Map as parameter should return every value inside it.
    * Prototype :
        * static User fromJson(Map<dynamic, dynamic> userJson)
* Create a method call toString that returns a string => User(id : id ,name: name, age: age, height: height);
    * Prototype :
        * String toString()
```
youssef@Holberton/Dart$ cat 5-main.dart
import '5-json_to_user.dart';

void main() {
  final djo = User(id: 1, name: "Djo", age: 25, height: 1.89);
    print(djo.toJson());
  Map map = {'id': 3, 'name': 'Youssef', 'age': 26, 'height': 1.9};
  final youssef = User.fromJson(map);
  print(djo.toString());
  print(youssef.toString());
}
youssef@Holberton/Dart$ dart 5-main.dart 
{id: 1, name: Djo, age: 25, height: 1.89}
User(id : 1 ,name: Djo,  age: 25, height: 1.89)
User(id : 3 ,name: Youssef,  age: 26, height: 1.9)
youssef@Holberton/Dart$
```
## 6. Inheritance
* Copy the class Password from 4-mutables.dart -> 6-password.dart:
* Copy the last task and extend the Password class to User
* Create a new property in the User class called user_password that contain the password.
* Add null check to all targets in 6-password.dart and null coalescing operator if necessary.
* Call isValid method from Password class after you passed user_password to Password class.
```
youssef@Holberton/Dart$ cat 6-main.dart
import '6-inheritance.dart';

void main() {
  final djo = User(
      id: 1, name: "Djo", age: 25, height: 1.89, user_password: "Azert23defde");
  print('<===========Json=========>:');
  print('\n');
  print(djo.toJson());
  Map map = {
    'id': 3,
    'name': 'Youssef',
    'age': 26,
    'height': 1.9,
    'user_password': "Azert23defde"
  };
  final youssef = User.fromJson(map);
  print('\n');
  print('<===========Test1===========>:');
  print('\n');
  print(djo.toString());
  print(youssef.toString());
  print('\n');
  print('<===========Test2===========>:');
  print('\n');
  djo.user_password = "holberton98";
  youssef.user_password = "AZERfghn6789";
  print(djo.toString());
  print(youssef.toString());
}
youssef@Holberton/Dart$ dart 6-main.dart
<===========Json=========>:


{id: 1, name: Djo, age: 25, height: 1.89}


<===========Test1===========>:


User(id : 1 ,name: Djo, age: 25, height: 1.89, Password: true)
User(id : 3 ,name: Youssef, age: 26, height: 1.9, Password: false)


<===========Test2===========>:


User(id : 1 ,name: Djo, age: 25, height: 1.89, Password: false)
User(id : 3 ,name: Youssef, age: 26, height: 1.9, Password: true)
youssef@Holberton/Dart$
```