# css 3
=======================

Packages
-----

- [purecss](https://purecss.io)


Tools
-----

- [ColorBox](https://lyft-colorbox.herokuapp.com)

- [CSS3 Transform Generator](https://html-css-js.com/css/generator/transform/)

### LINKS

- [CSS ](https://en.owl.institute/web-interface-design/css-basics/flexible-layouts-using-flexbox-all-flexbox-properties-at-a-glance)
- [CSS Flex Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

- [Designify-me](http://designify.me/)
-----------------------------------------------------------------------------------------------------

## FONTS

- [HACK](https://sourcefoundry.org/hack/)
- [HACK --github--](https://github.com/source-foundry/Hack/blob/master/docs/WEBFONT_USAGE.md)


## Icons

- [devicon.dev](https://devicon.dev/)
- [icons8](https://icons8.com/)

## ::before ::after

The ::before and ::after pseudo-elements in CSS allows you to insert content onto a page without it needing to be in the HTML. While the end result is not actually in the DOM, it appears on the page as if it is, and would essentially be like this:


```

div::before {
  content: "before";
}
div::after {
  content: "after";
}

```


```

<div>
  before
  <!-- Rest of stuff inside the div -->
  after
</div>

```

## tabindex

- [Source](https://webaim.org/techniques/keyboard/tabindex)

```
[tabindex="-1"]:focus:not(:focus-visible)
```
The tabindex attribute explicitly defines the navigation order for focusable elements (typically links and form controls) within a page. It can also be used to define whether elements should be focusable or not.

[Both] tabindex="0" and tabindex="-1" have special meaning and provide distinct functionality in HTML. A value of 0 indicates that the element should be placed in the default navigation order. This allows elements that are not natively focusable (such as <div>, <span>, and <p>) to receive keyboard focus. Of course one should generally use links and form controls for all interactive elements, but this does allow other elements to be focusable and trigger interaction.

A tabindex="-1" value removes the element from the default navigation flow (i.e., a user cannot tab to it), but it allows it to receive programmatic focus, meaning focus can be set to it from a link or with scripting.** This can be very useful for elements that should not be tabbed to, but that may need to have focus set to them.

## prefers-reduced-motion

- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)


* **no-preference**
    Indicates that the user has made no preference known to the system.

* **reduce**

    Indicates that user has notified the system that they prefer an interface that removes or replaces the types of motion-based animation that trigger discomfort for those with vestibular motion disorders. 

-----------------------------------------------------------------------------------------------------

# FLEX

**flex**:  flex-grow | flex-shrink | flex-basis.

### flex-basis

Defines the preferred width for an element. If an element does not fit into a container, it can still be reduced in size. The default value is auto, i. e. the width of the element is based on its content.

```
.element {
    -ms-flex-preferred-size: <width specification>;
    -webkit-flex-basis: <width specification>;
    flex-basis: <width specification>;
}

```

### flex-grow

This property specifies whether a flex element should be increased in size if necessary. The value assigned to this property is a number specifying the proportion of space available in the container which the element should take up. E. g. if you assign flex-grow: 1 to all elements, they will be distributed equally, i. e. they will all have the same width (top row in figure). If one of the elements is assigned a value of 2, it will take up twice as much space, i.e. it will be twice as wide as the other elements (bottom row in figure).

```

.element {
    -ms-flex-positive: <number>;
    -moz-box-flex: <number>;
    -webkit-box-flex: <number>;
    -webkit-flex-grow: <number>;
    flex-grow: <number>;
}

```
-----------------------------------------------------------------------------------------------------

## Features


Firefox 3.6+ 		-moz 	-moz-linear-gradient
Chrome, Safari 4 		-webkit 	-webkit-gradient
Crhome 10+, Safari 5.1+ 		-webkit 	-webkit-linear-gradient
Opera 11.10+ 		-o 	-o-linear-gradient
Internet Explorer 6-9 		filter 	filter
Internet Explorer 10+ 		-ms 	-ms-linear-gradient
Estándar W3C 	– 	Ninguno 	linear-gradient
Navegadores antiguos 	– 	Sin soporte 	No soportan etiquetas de CSS3.


```
-webkit-column-count: 3;
-webkit-column-gap: 10px;
-webkit-column-fill: auto;
-moz-column-count: 3;
-moz-column-gap: 10px;
-moz-column-fill: auto;


```




-----------------------------------------------------------------------------------------------------