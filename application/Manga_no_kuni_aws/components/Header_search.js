import React from 'react';
import { View, StyleSheet , TouchableOpacity, Image, Text} from 'react-native';
import { SearchBar } from 'react-native-elements';

// themes import 
import * as light_theme from '../assets/themes/light';
import * as dark_theme from '../assets/themes/dark';
import * as app_common_style from '../assets/themes/common_style';

const HeaderSearch = (props) => {

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

        SearchBar_global_container : {
            flex : 1,
            flexDirection: "row",
            alignItems: 'center', 
            marginLeft : 20,
            marginRight : 5
        },

        SearchBar_container : {
            backgroundColor : (props.dark) ? dark_theme.home_header_color : light_theme.home_header_color,
            borderTopWidth : 0,
            borderBottomWidth : 0,
            flex : 1,
            marginVertical : 1
        },

        SearchBar_clear_icon :{
            color : (props.dark) ? dark_theme.text_color : light_theme.text_color,
            marginHorizontal : 10
        }


    });



    return (
    <View style = {styles.container}>
        <TouchableOpacity onPress = {props.toogle}>
            <Image
                source= {require('../assets/drawerButton/drawerDark.png')}
                style={styles.drawerButton}
            />
        </TouchableOpacity>

        <View style = {styles.SearchBar_global_container}>
            
            <SearchBar
                platform="default"
                containerStyle={styles.SearchBar_container}
                inputContainerStyle={{backgroundColor : 'white'}}
                inputStyle={{}}
                leftIconContainerStyle={{}}
                rightIconContainerStyle={{}}
                loadingProps={{}}
                onChangeText={newVal => newVal}
                //onClearText={() => console.log(onClearText())}
                placeholder="Type query here..."
                placeholderTextColor="#888"
                round
                //onCancel={() => console.log(onCancel())}
                //value={value}
            />
                    
            <TouchableOpacity >
                <Text style = {styles.SearchBar_clear_icon} >Clear</Text>
            </TouchableOpacity>

        </View>


    </View>
    );
}

export default HeaderSearch;