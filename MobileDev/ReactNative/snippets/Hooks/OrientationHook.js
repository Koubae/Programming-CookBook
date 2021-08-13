// CREDITS -->
// https://stackoverflow.com/a/61838183/13903942
// https://stackoverflow.com/a/51127926/13903942

import {useEffect, useState} from 'react';
import {Dimensions} from 'react-native';

const isPortrait = () => {
    const dim = Dimensions.get('screen');
    return dim.height >= dim.width;
};

export function useOrientation() {  
    const [orientation, setOrientation] = useState(isPortrait() ? 'PORTRAIT' : 'LANDSCAPE');
    useEffect(() => {
        const callback = () => setOrientation(isPortrait() ? 'PORTRAIT' : 'LANDSCAPE');
        Dimensions.addEventListener('change', callback);
        return () => {
            Dimensions.removeEventListener('change', callback);
        };
    }, []);

    return orientation;
}



// USAGE

import React from 'react';
import { View  } from 'react-native';
import { useOrientation } from '../themes/Orientation';
const Container = ({ children }) => { 
    console.log("useOrientation", useOrientation)

    const orientation = useOrientation();
return(
    <View style={ containerStyles.container }>
    {
        children
    }
    </View>
)};
