<?php // Credit https://flowframework.readthedocs.io/en/stable/TheDefinitiveGuide/PartV/CodingGuideLines/index.html

// The keyword 'use' has two different applications, but the reserved word table links to here.

// It can apply to namespace constucts:

?>

<!-- file1: -->
<?php namespace foo;

class Cat {
    static function says() {echo 'meoow';}  
} 
?>


<!-- file2 -->
<?php namespace bar;

class Dog {
    static function says() {echo 'ruff';}  
} 

?>


<!-- file3: -->
<?php namespace animate;
class Animal {
    static function breathes() {echo 'air';}  
} 
?>


<!-- file4: -->
<?php namespace fub;
    include 'file1.php';
    include 'file2.php';
    include 'file3.php';
    use foo as feline;
    use bar as canine;
    use animate;

    echo \feline\Cat::says(), "<br />\n";
    echo \canine\Dog::says(), "<br />\n";
    echo \animate\Animal::breathes(), "<br />\n";  
?>


<!-- 

Note that
felineCat::says()
should be
\feline\Cat::says()
(and similar for the others)
but this comment form deletes the backslash (why???)

The 'use' keyword also applies to closure constructs:

-->

<?php function getTotal($products_costs, $tax)
    {
        $total = 0.00;
       
        $callback =
            function ($pricePerItem) use ($tax, &$total)
            {
               
                $total += $pricePerItem * ($tax + 1.0);
            };
       
        array_walk($products_costs, $callback);
        return round($total, 2);
    }
?>

