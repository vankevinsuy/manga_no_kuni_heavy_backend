import React from 'react';

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import SplashScreen from './Activities/SplashScreen';
import ConnectionInscription from './Activities/ConnectionInscription';
import Home from './Activities/Home';

const Stack = createStackNavigator();

const App  = () => {
    return (
      <NavigationContainer>

        <Stack.Navigator initialRouteName="SplashScreen" headerMode="none">

          <Stack.Screen name="SplashScreen" component={SplashScreen}  />
          <Stack.Screen name="ConnectionInscription" component={ConnectionInscription} />
          <Stack.Screen name="Home" component={Home} />

        </Stack.Navigator>

      </NavigationContainer>

    );
}

export default App;