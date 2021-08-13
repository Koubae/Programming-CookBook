import React, {useState, useRef, useEffect} from 'react';
import { SafeAreaView, StatusBar, StyleSheet, Text, View , Animated} from 'react-native';
// import type {Node} from 'react';  wrap App to const App: () => Node = ()
import type {Node} from 'react'; 


function useInterval(callback, delay) {
    const savedCallback = useRef();
    // Remember the latest callback.
    useEffect(() => {
        savedCallback.current = callback;
    }, [callback]);
    // Set up the interval.
    useEffect(() => {
        function tick() {
        savedCallback.current();
        }
        if (delay !== null) {
        let id = setInterval(tick, delay);
        return () => clearInterval(id);
        }
    }, [delay]);
}

// const App: () => Node = () => {
const App = () => {


    let animation = useRef(new Animated.Value(0));
    const [progress, setProgress] = useState(0);
    console.log(animation)
    console.log("progress >", progress)
    useInterval(() => {
        if(progress < 100) {
            setProgress(progress + 5);
        } else {
            setProgress(progress - 100 )
        }
    }, 1000);
    // Animation

    useEffect(() => {
        Animated.timing(animation.current, {
            toValue: progress,
            duration: 100,
            useNativeDriver: false
        }).start();
    }, [progress])

    const width = animation.current.interpolate({
        inputRange: [0, 100],
        outputRange: ["0%", "100%"],
        extrapolate: "clamp"
    })


    return (
        <SafeAreaView style={ style.body}> 
        <StatusBar
            backgroundColor="#31DAFF"
            barStyle={'dark-content'}             
        />  
            <View style={ style.container }>
                <View style={ style.banner}>
                    <Text style={style.banner__Title}>
                        Convert
                    </Text>
                </View>

                <View style={ style.container, style.progresBarWrapper}>
                    <Text style={style.progressText}> Loading ...... </Text>
                    <View style={ style.progressBar}>
                    {/* {backgroundColor: "#8BED4F", width } */}
                        {/* <Animated.View style={ [StyleSheet.absoluteFill], style.progressBarBar
                         }
                        /> */}

                      <Animated.View style={[StyleSheet.absoluteFill, { backgroundColor: "#8BED4F", width }]}/>

                    </View>
                    <Text style={style.progressText}> { `${progress}%` } </Text>
                </View>
                
            </View>

           
        </SafeAreaView>
       
    );
};

const style = StyleSheet.create({
    body: {
        backgroundColor: "#343333",
        flex: 1,
    },

    container: {
        paddingHorizontal: 30,
        marginTop: 40
    },

    banner:  {
        paddingHorizontal: 40,
        paddingVertical: 40,
        backgroundColor:  "#F3F3F3",        
        borderRadius: 20,
        backgroundColor: "rgba(49, 218, 255, 0.45)",
    },

    banner__Title : {
        fontSize: 30,
        fontWeight: "800",
        textAlign: "center",
        textTransform: "uppercase",  
        color: "white",
        fontStyle: "italic"
        
    },

    textInput:  {
        paddingHorizontal: 40,
        paddingVertical: 20,
        backgroundColor:  "#F3F3F3",
        borderStyle: "solid",
        borderWidth: 2,
        borderColor: "#31DAFF",
        borderRadius: 20
    },

    // progresBarWrapper: {
    //     flex: 1,
    // },

    progressBar: {
        marginVertical: 10,
        height: 20,
        width: '100%',
        backgroundColor: 'white',
        borderColor: '#000',
        borderWidth: 2,
        borderRadius: 20
    },
    progressBarBar: {
        backgroundColor: "#8BED4F",
        width: "100%"
    },

    progressText: {
        fontSize: 20,
        textAlign: "center",
        color: "white"
    }

});


export default App;
