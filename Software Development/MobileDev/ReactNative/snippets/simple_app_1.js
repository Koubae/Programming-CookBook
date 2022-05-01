import React, { useState } from 'react';
import type {Node} from 'react';
import {
    SafeAreaView,
    ScrollView,
    StatusBar,
    StyleSheet,
    Text,
    useColorScheme,
    View,
    Dimensions ,
    TouchableOpacity,
    TextInput,
    Platform,
    KeyboardAvoidingView,
    Keyboard
} from 'react-native';

import {
    Colors,
} from 'react-native/Libraries/NewAppScreen';




// App
const App: () => Node = () => {
    const isDarkMode = useColorScheme() === 'dark';
    const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.light,
    };
    let ScreenHeight = Dimensions.get("window").height;

    // ------------ useStates
    const [task, setTask] = useState();
    const [taskItems, setTaskItems] = useState([]);

    // Functions
    const handleAddTask = () => {          
        Keyboard.dismiss();
        setTaskItems([...taskItems, task]);
        setTask(null);
    }

    const completeTask = (index) => {
        let itemsCopy = [...taskItems];
        itemsCopy.splice(index, 1);
        setTaskItems(itemsCopy)
    }

    // components
    const Section = ({children,  title}): Node => {

        const isDarkMode = useColorScheme() === 'dark';
        return (
        <View style={styles.sectionContainer}>
            <View style={styles.banner}>
                <Text
                    style={[
                        styles.sectionTitle,
                        {
                        color: isDarkMode ? Colors.white : Colors.black,
                        },
                    ]}>
                    {title}
                </Text>
            </View>

        
            {
            children ?
                children.map( (item, idx) => {             
                    return (
                        <TouchableOpacity key={ idx } style={ styles.sectionItem }
                        onPress={ () => completeTask(idx)}
                        >

                            <View style={styles.itemLeft}>
                                <View style={styles.square}></View>
                                <Text key={ idx } style={ [styles.item, { color:  isDarkMode ? Colors.white : Colors.black}]}>
                                    { item }
                                </Text>
                            </View>
                            <View style={styles.circular}></View>
                        </TouchableOpacity>     
                    ) 
                }) 
                :  <></>
            }

        </View>
        );
    };

    return (
    <SafeAreaView style={backgroundStyle}>
        <StatusBar barStyle={!isDarkMode ? 'light-content' : 'dark-content'} />
        <View style={styles.mainContainer, {height: ScreenHeight, backgroundColor: isDarkMode}}>
            <ScrollView 
                contentContainerStyle={{ flexGrow: 1 }}
                keyboardShouldPersistTaps='handled'>

                <Section title="Todo list">

                    {
                        taskItems.map( (item, idx) => {
                            return (
                                <Text key={ idx }> {item} </Text>
                            )
                        })
                    }

                </Section>
            </ScrollView>

            <KeyboardAvoidingView 
                behavior={ Platform.OS === 'ios' ? 'padding' : 'height' }
                style={styles.userInputWrapper}>
                <TextInput 
                    style={styles.input} 
                    placeholder={'Write...'} 
                    value={task}
                    onChangeText={text => setTask(text)} 
                />
                <TouchableOpacity onPress={() => handleAddTask()}>                    
                    <View style={ styles.userInputContainer}>
                        <Text style={styles.addBtn}>+</Text>
                    </View>
                </TouchableOpacity>
            </KeyboardAvoidingView>


        </View>
        
        
    
    </SafeAreaView>
    
    );
};

const styles = StyleSheet.create({
    mainContainer: {
        flex: 1,
    },

    sectionContainer: {
        paddingTop: 40,
        paddingHorizontal: 40,
        marginTop: 20,
        justifyContent: 'space-around',
        alignItems: 'center'
    },

    banner: {
        marginBottom: 30,
        paddingHorizontal: 40,
        paddingVertical: 20,
        backgroundColor: '#F3F3F3',
        width: "100%",
        borderRadius: 10
    },

    sectionTitle: {
        fontSize: 40,
        fontWeight: "800",
        textAlign: "center",
        textTransform: "uppercase",        

    },

    sectionItem: {
        marginBottom: 20,
        paddingHorizontal: 40,
        paddingVertical: 10,        
        backgroundColor: '#F3F3F3',
        borderRadius: 10,
        width: "80%",

        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
    },

    item: {
        fontSize: 20,
        fontWeight: "400",
        textAlign: "center"
    },

    itemLeft: {
        flexDirection: "row",
        alignItems: "center",
        flexWrap: "wrap"
    },

    square: {
        width: 20,
        height: 20,
        backgroundColor: '#1292B4',
        opacity: 0.4,
        borderRadius: 5,
        marginRight: 15,
    },
    circular: {
        width: 12,
        height: 12,
        borderColor: '#1292B4',
        borderWidth: 2,
        borderRadius: 5,
    },

    userInputWrapper: {
        marginBottom: 40,
        paddingHorizontal: 30,
        width: "100%",
        flexDirection: "row",
        justifyContent: "space-around",
        alignItems: "center"
    },

    input: {
        paddingVertical: 15,
        paddingHorizontal: 15,
        backgroundColor: '#F3F3F3',
        borderColor: "#C0C0C0",
        borderWidth: 1,
        borderRadius: 30,
        width: "80%"
        

    },

    userInputContainer: {
        width: 60,
        height: 60,
        backgroundColor: '#F3F3F3',
        borderRadius: 60,
        justifyContent: 'center',
        alignItems: 'center',
        borderColor: '#C0C0C0',
        borderWidth: 1,
    },

    addBtn: {},




});

export default App;
