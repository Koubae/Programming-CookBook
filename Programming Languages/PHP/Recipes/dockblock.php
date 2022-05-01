// dockblock zend style   https://framework.zend.com/manual/1.12/en/coding-standard.coding-style.html

/*
The @category annotation must have a value of "Zend".

The @package annotation must be assigned, and should be equivalent to the component name of the class contained in the file; 
typically, this will only have two segments, the "Zend" prefix, and the component name.

The @subpackage annotation is optional. If provided, it should be the subcomponent name, minus the class prefix. 
In the example above, the assumption is that the class in the file is either "Zend_Magic_Wand", or uses that classname as part of its prefix.
*/

/**
* Short description for file
*
* Long description for file (if any)...
*
* LICENSE: Some license information
*
* @category   Zend
* @package    Zend_Magic
* @subpackage Wand
* @copyright  Copyright (c) 2005-2015 Zend Technologies USA Inc. (http://www.zend.com)
* @license    http://framework.zend.com/license   BSD License
* @version    $Id:$
* @link       http://framework.zend.com/package/PackageName
* @since      File available since Release 1.5.0
*/


// Every class must have a docblock that contains these phpDocumentor tags at a minimum:

/**
* Short description for class
*
* Long description for class (if any)...
*
* @category   Zend
* @package    Zend_Magic
* @subpackage Wand
* @copyright  Copyright (c) 2005-2015 Zend Technologies USA Inc. (http://www.zend.com)
* @license    http://framework.zend.com/license   BSD License
* @version    Release: @package_version@
* @link       http://framework.zend.com/package/PackageName
* @since      Class available since Release 1.5.0
* @deprecated Class deprecated in Release 2.0.0
*/
