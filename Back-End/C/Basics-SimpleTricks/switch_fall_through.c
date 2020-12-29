
// FALL THROUGH
void func()
{
  int someVariable;

  

  switch (someVariable) {
  case 1:
    printf("This code handles case 1\n");
    break;
  case 2:
    printf("This prints when someVariable is 2, along with...\n");
    /* FALL THROUGH */  


  case 3:
    printf("This prints when someVariable is either 2 or 3.\n" );
    break;
  }

 }

// fall-through comment is not necessary here because the intended behavior is obvious) 

void func()
{
  int something;
  switch(something) {
    case 2:
    case 3:
    case 4:
      /* some statements to execute for 2, 3 or 4 */
      break;
    case 1:
    default:
      /* some statements to execute for 1 or other than 2,3,and 4 */
      break;
 }
}
