class Config
{
    private $values = [];

    // return a REFERENCE to the actual $values array
    public function &getValues() { // Add & in order to return $values by reference and not a copy of it .
        return $this->values;
    }
}

$config = new Config();

$config->getValues()['test'] = 'test';
echo $config->getValues()['test'];


// Using a PHP Object instead of an arrayclass Config

{
    private $values;

    // using ArrayObject rather than array
    public function __construct() {
        // unlike arrays, PHP always passes objects by reference
        // ArrayObject is an SPL object, which fully mimics arrays usage, but works as an object.
        $this->values = new ArrayObject();
    }

    public function getValues() {
        return $this->values;
    }
}

$config = new Config();

$config->getValues()['test'] = 'test';
echo $config->getValues()['test'];

// it is important to note that the practice of returning a reference to an array or an ArrayObject 
is generally something that should be avoided, as it provides the caller with the ability to modify the instance’s private data. 
This “flies in the face” of encapsulation. Instead, it’s better to use old style “getters” and “setters”

class Config
{
    private $values = [];
    
    public function setValue($key, $value) {
        $this->values[$key] = $value;
    }
    
    public function getValue($key) {
        return $this->values[$key];
    }
}

$config = new Config();

$config->setValue('testKey', 'testValue');
echo $config->getValue('testKey');    // echos 'testValue'