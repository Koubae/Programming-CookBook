/*
NOT EXPO PROJECT!!! RUN:

npm install @react-navigation/native @react-navigation/stack
npm install react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view

May Need installation:

    npm install typescript

*/ 



import 'react-native-gesture-handler';
import * as React from 'react';
import {View, Text, TextInput, Button,} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';


const HomeScreen = ({ navigation }) => {
return (
<View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
    <Text>Home Screen</Text>
<Button
    title="Go to Details"
    onPress={() => navigation.navigate('Details', {
        itemId: 86,
        otherParam: 'Other Param'
    })}
    />

<Button
    title="PROFILE"
    onPress={() => navigation.navigate('Profile', { title: "My Profile" })}
    />
</View>
);};

const DetailsScreen = ({ route, navigation }) => {

const { itemId, otherParam } = route.params;
return (
<View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
    <Text> Details Screen </Text>
    <Text>itemId: { JSON.stringify(itemId) }</Text>
    <Text>OtherParam: { JSON.stringify(otherParam)}</Text>
    <Button
        title="Go to Details... again"
        onPress={() => navigation.push('Details', {
            itemId: Math.floor(Math.random() * 100),
        })}
    />
    {/* GO BACK HOME */}
    <Button title="Go to Home" onPress={ () => navigation.navigate('Home') } />
    {/* GO BACK ONE SCREEN */}
    <Button title="Go back" onPress={ () => navigation.goBack() } />
    {/* TO FIRST SCREEN (OLDER) IN STACK */}
    <Button
        title="Go back to first screen in stack"
        onPress={() => navigation.popToTop() }/>

    {/* setParam on the fly */}
    <Button 
        title="Switch Params Data"
        onPress={ () => navigation.setParams({ itemId: route.params.itemId === 99999 ? 12398 : 99999 })} />

</View>
);}


// DEMOSTRATING SET OPTIONS
const ProfileScreen = ({ navigation, route }) => { 

const [value, onChangeText] = React.useState(route.params.title);

React.useLayoutEffect( () => {
    navigation.setOptions({
        title: value === '' ? 'No title' : value,
    });
}, [navigation, value]);

return (

<View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
    <TextInput style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
        onChangeText={ onChangeText }
        value={ value }
    />

    <Button title='Go Back' onPress={ () => navigation.goBack() } />

</View>

);}

const Stack = createStackNavigator();

const App = () => {
return (

<NavigationContainer>
    <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={ HomeScreen } options={{ title: 'Overview' }}/> 
        <Stack.Screen name="Details" component={ DetailsScreen } initialParams={{ itemId: 123789 }}/>
        <Stack.Screen name="Profile" component={ ProfileScreen } options={({ route }) => ({ title: route.params.title })}/>
    </Stack.Navigator>
</NavigationContainer>


);
};

export default App;