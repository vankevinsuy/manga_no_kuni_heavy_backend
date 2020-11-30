import React, { useState } from 'react';
import { SafeAreaView,  View,  StyleSheet,  Image,  Text, } from 'react-native';
import {  DrawerContentScrollView,  DrawerItemList,  DrawerItem,} from '@react-navigation/drawer';
import {getUsername} from '../CustomFunctions/CommonVariable'

import Amplify, { Auth } from 'aws-amplify';
import config from '../aws-exports';
Amplify.configure(config);


const CustomSidebarMenu = (props) => {

  const [userName, setUserName] = useState("none");
  getUsername().then((val) =>setUserName(val));

  return (
    <SafeAreaView style={{flex: 1}}>

      <Image
        source={require('../assets/default_profile.png')}
        style={styles.sideMenuProfileIcon}
      />
      <Text  style={styles.user_name}>{userName}</Text>

      <DrawerContentScrollView {...props}>
        <DrawerItemList {...props} />


      </DrawerContentScrollView>

    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  sideMenuProfileIcon: {
    resizeMode: 'contain',
    width: 150,
    height: 150,
    alignSelf: 'center',
    marginTop : 10
  },
  user_name : {
    alignSelf : 'center',
    fontSize : 20
  }
});

export default CustomSidebarMenu;