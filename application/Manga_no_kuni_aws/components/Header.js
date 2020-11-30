import React from 'react';
import { View, StyleSheet , TouchableOpacity, Image, Text} from 'react-native';
import { SearchBar } from 'react-native-elements';

// themes import 
import * as light_theme from '../assets/themes/light';
import * as dark_theme from '../assets/themes/dark';
import * as app_common_style from '../assets/themes/common_style';

const Header = (props) => {

    const styles = StyleSheet.create({
        container: {
          flex: 0.15,
          alignItems: 'center', 
          backgroundColor : (props.dark) ? dark_theme.home_header_color : light_theme.home_header_color,
          flexDirection: "row",
        }, 
        drawerButton : {
            width: 40, 
            height: 40,
            marginLeft: 10
        },
    });



    return (
    <View style = {styles.container}>
        <TouchableOpacity onPress = {props.toogle}>
            <Image
                source= {require('../assets/drawerButton/drawerDark.png')}
                style={styles.drawerButton}
            />
        </TouchableOpacity>

    </View>
    );
}

export default Header;