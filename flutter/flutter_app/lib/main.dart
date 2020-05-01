import 'package:flutter/material.dart';

main(){
  runApp(MyaApp());
}

  class MyaApp extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title : Text("hello Pro"),
        ),
        body: Center(
          child: Text("Hello"),)

      )
  );
  }
}