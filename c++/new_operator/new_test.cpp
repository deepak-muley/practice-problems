// operator new[] example
#include <iostream>     // std::cout
#include <new>          // ::operator new[]

struct MyClass {
  int data;
  MyClass() {std::cout << '*';}  // print an asterisk for each construction
};

int test() {
  int* p = new int[100];
  for(int i=0; i < 100; i++){
     std::cout << p[i];
  }
  std::cout << '\n';

  int* q = new int[100]();
  for(int i=0; i < 100; i++){
     std::cout << q[i];
  }
  std::cout << '\n';
}

int main () {
  int p[1000] = {1, };
  for(int i=0; i < 1000; i++){
     std::cout << p[i];
  }
  std::cout << '\n';

  std::cout << "constructions (1): ";
  // allocates and constructs five objects:
  MyClass * p1 = new MyClass[5];
  std::cout << '\n';

  std::cout << "constructions (2): ";
  // allocates and constructs five objects (nothrow):
  MyClass * p2 = new (std::nothrow) MyClass[5];
  std::cout << '\n';

  std::cout << "constructions (3): ";
  // allocates storage for five objects, but does not construct them:
  MyClass * p3 = static_cast<MyClass*> (::operator new (sizeof(MyClass[5])));
  std::cout << '\n';

  std::cout << "constructions (4): ";
  // constructs five objects at p3, but does not allocate:
  new (p3) MyClass[5];
  std::cout << '\n';

  std::cout << "constructions (5): ";
  // constructs five objects at p3, but does not allocate:
  new (p3) MyClass[5]();
  std::cout << '\n';

  delete[] p3;
  delete[] p2;
  delete[] p1;

  test();

  return 0;
}
