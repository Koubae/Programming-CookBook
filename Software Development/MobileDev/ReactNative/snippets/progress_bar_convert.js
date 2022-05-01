import React, {useState, useRef, useEffect} from 'react';
import { 
    SafeAreaView, 
    StatusBar, 
    StyleSheet, 
    Text, 
    View , 
    Animated, 
    TextInput,
    KeyboardAvoidingView,
    TouchableOpacity,
    TouchableHighlight,
    Button,
    Alert 
    
    } from 'react-native';
// import type {Node} from 'react';  wrap App to const App: () => Node = ()
// import type {Node} from 'react'; 


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
                {/* Banner */}
                <View style={ style.banner}>
                    <Text style={style.banner__Title}>
                        Status
                    </Text>
                </View>
                {/* Progress Bar */}
                <View style={ style.container, style.progresBarWrapper}>
                    <Text style={style.progressText}> Loading ...... </Text>
                    <View style={ style.progressBar}>
                        <Animated.View style={[StyleSheet.absoluteFill, style.progressBarBar, { width }]}/>
                    </View>
                    <Text style={style.progressText}> { `${progress}%` } </Text>
                </View>               

            </View>

            <View style={ style.tray}>
          
            </View>

             {/* User Input */}
            
          
            <KeyboardAvoidingView 
                behavior={ Platform.OS === 'ios' ? 'padding' : 'height' }
                style={ style.container, style.userInputWrapper }>   
                    <View style={ style.btn}>
                        <Button
                            // onPress={onPressLearnMore}
                            onPress={() => Alert.alert('Simple Button pressed')}
                            title="CONVERT"
                            color="rgba(49, 218, 255, 0.45)"
                            accessibilityLabel="Learn more about this purple button"
                        />
                    </View>

                    <TextInput 
                    style={ style.userInputBox}
                    placeholder={'Write...'} 

                
                />
            </KeyboardAvoidingView>


           
        </SafeAreaView>
       
    );
};

const style = StyleSheet.create({
    body: {
        backgroundColor: "#1C1D1D",  // "#343333",
        flex: 1,
    },

    container: {
        paddingHorizontal: 30,
        marginVertical: 40
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

    progressBar: {
        marginVertical: 10,
        height: 20,
        width: '100%',
        backgroundColor: 'white',
        borderColor: "#8BED4F",
        borderWidth: 2,
        borderRadius: 20
    }, 

    progressBarBar: {
        // backgroundColor: "#8BED4F"
        backgroundColor: "#31DAFF",
    },

    progressText: {
        fontSize: 20,
        textAlign: "center",
        color: "white"
    },

    tray: {
        marginBottom: 20,
        paddingVertical: 100,
     },

    userInputWrapper: {
        flexDirection: "column",
        justifyContent: "space-around",
        alignItems: "center",
        width: "100%",
        
    },

    userInputBox:  {
        paddingHorizontal: 100,
        width: "80%",
        paddingVertical: 10,
        backgroundColor:  "#F3F3F3",
        borderStyle: "solid",
        borderWidth: 2,
        borderColor: "#8BED4F",
        borderRadius: 20
    },
    
    btn: {
        marginBottom: 20,
        width: "80%"

    }

});


export default App;
