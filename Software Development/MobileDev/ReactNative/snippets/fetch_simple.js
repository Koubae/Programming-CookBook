import React, {useState, useEffect} from 'react';
import { 
    ActivityIndicator,
    FlatList,
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

// CONSTANTS
const MAINTHEME_BKG = "#f8f8f8";
const MAINTHEME_COLOR = "#6ba3ff";
const MAINTHEME_SUBCOLOR = "#2c3e50";


function makeRequest() {
    console.log("Hello Word")
}

// const App: () => Node = () =>{
const App = () => {

    const [isLoading, setLoading] = useState(true);
    const [data, setData] = useState([]);
    if (isLoading) {
        fetch('https://reactnative.dev/movies.json')
            .then((response) => response.json())
            .then((json) => setData(json.movies))
            .catch((error) => console.error(error))
            .finally(() => setLoading(false));
    }

    return (
        <SafeAreaView style={ style.body}> 
        <StatusBar
            backgroundColor={ MAINTHEME_COLOR }
            barStyle={'dark-content'}             
        />  
            <View style={ style.container }>
                {/* Banner */}
                <View style={ style.banner}>
                    <Text style={style.banner__Title}>
                        Status
                    </Text>
                </View>


            </View>

            <View style={ style.tray}>
        
                <View style={{ padding: 25}}>     
                    {
                        isLoading ? <ActivityIndicator size="large" color="#00ff00"/> 
                        : (
                        <FlatList
                            data={ data }
                            keyExtractor={({ id }, idx) => id}
                            renderItem={({ item }) => (
                                <Text style={[style.defaultText]}>{item.title}, {item.releaseYear}</Text>
                            )}
                        />
                        )
                    }
                </View>
            </View>

             {/* User Input */}
            
          
            <KeyboardAvoidingView 
                behavior={ Platform.OS === 'ios' ? 'padding' : 'height' }
                style={ style.container, style.userInputWrapper }>   
                    <View style={ style.btn}>
                        <Button
                            // onPress={onPressLearnMore}
                            onPress={ makeRequest }
                            title="REQUEST"
                            color={ MAINTHEME_COLOR }
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
        backgroundColor: MAINTHEME_BKG, 
        flex: 1,
    },

    container: {
        paddingHorizontal: 30,
        marginVertical: 40,

    },

    banner:  {
        paddingHorizontal: 40,
        paddingVertical: 40,  
        backgroundColor: MAINTHEME_COLOR, 
        borderRadius: 20,
        borderStyle: "solid",
        borderWidth: 2,
        borderColor: MAINTHEME_SUBCOLOR,
    },

    banner__Title : {
        fontSize: 30,
        fontWeight: "800",
        textAlign: "center",
        textTransform: "uppercase",  
        color: "white",
        fontStyle: "italic",
    
        
    },    

    tray: {
        marginBottom: 20,
        paddingVertical: 100,
    },

    defaultText: {
        fontSize: 20,
        fontWeight: "800",
        textAlign: "center",
        textTransform: "uppercase",  
        color: "black",
        fontStyle: "italic",
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
        borderColor: MAINTHEME_SUBCOLOR,
        borderRadius: 20
    },
    
    btn: {
        marginBottom: 20,
        width: "80%"

    }

});


export default App;