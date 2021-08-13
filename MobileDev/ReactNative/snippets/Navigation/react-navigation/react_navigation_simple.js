/*
NOT EXPO PROJECT!!! RUN:

npm install @react-navigation/native @react-navigation/stack
npm install react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view

May Need installation:

    npm install typescript

*/ 


/* SIMPLE NAVIGATION*/ 

import 'react-native-gesture-handler';
import * as React from 'react';
import {Text, Button,} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';


const HomeScreen = ({ navigation }) => {
return (
<Button
    title="Go to Jane's profile"
    onPress={() =>
    navigation.navigate('Profile', { name: 'Jane' })
    }
/>
);
};
const ProfileScreen = ({ navigation, route }) => {
    return <Text>This is {route.params.name}'s profile</Text>;
};

const Stack = createStackNavigator();

const App = () => {
return (

<NavigationContainer>
    <Stack.Navigator>
        <Stack.Screen
            name="Home"
            component={HomeScreen}
            options={{ title: 'Welcome' }}
        />
        <Stack.Screen name="Profile" component={ProfileScreen} />
    </Stack.Navigator>
</NavigationContainer>


);
};

export default App;