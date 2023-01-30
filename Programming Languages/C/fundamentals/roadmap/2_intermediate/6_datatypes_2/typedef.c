// ====== < typedef > ====== //

// We use the typedef keyword to create an alias name for data types. It is commonly used with structures to simplify the syntax of declaring variables.
// WARNING https://www.kernel.org/doc/Documentation/CodingStyle
// new -> https://www.kernel.org/doc/Documentation/process/coding-style.rst
// -> https://www.kernel.org/doc/html/v4.10/process/coding-style.html
/*
SOO https://stackoverflow.com/a/32405369/13903942


Please don't use things like "vps_t". It's a mistake to use typedef for structures and pointers. When you see a

vps_t a;

in the source, what does it mean? In contrast, if it says

 struct virtual_container *a;

you can actually tell what "a" is.

*/

// anonymous struct definitions
typedef struct {
    int x, y, z;
} vector3;

struct Distance{
    int feet;
    float inch;
};

int main() {
    struct Distance d1, d2;
}

// Equal to 
typedef struct Distance{
    int feet;
    float inch;
} distances;

int main() {
    distances d1, d2;
}

// forward declaring the struct, typedefing it, then defining the struct using the typedefd type for next

struct _queue_item;                           // 4

typedef struct _queue_item queue_item_t;      // 5

struct _queue_item {                          // 6
  vpoint_t void_item;
  queue_item_t* next;                         // 7
}

// opaque type  structure
// https://stackoverflow.com/a/252810/13903942

/*          
typedef struct Point Point;

typedef Point * point_new(int x, int y);

struct Point
{
  int x, y;
};

Point * point_new(int x, int y)
{
  Point *p;
  if((p = malloc(sizeof *p)) != NULL)
  {
    p->x = x;
    p->y = y;
  }
  return p;
}

*/