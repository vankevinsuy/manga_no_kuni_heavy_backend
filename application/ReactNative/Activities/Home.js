import React, { useState, useEffect } from "react";
import { StyleSheet, View , Image, BackHandler, Alert} from 'react-native';
import * as app_color from '../assets/themes/common_style';


const Home = () =>  {

    return (
        <View style={styles.container}>
            <Image
                style={styles.tinyLogo}
                source={{
                uri: 'https://reactnative.dev/img/tiny_logo.png',
                }}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
    },
    tinyLogo: {
        width: 50,
        height: 50,
      },
});

export default Home;