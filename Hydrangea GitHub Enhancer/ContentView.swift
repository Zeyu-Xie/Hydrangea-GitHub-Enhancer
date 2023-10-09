//
//  ContentView.swift
//  Hydrangea GitHub Enhancer
//
//  Created by Acan on 2023/10/9.
//

import SwiftUI

struct FirstView: View {
    var body: some View {
        NavigationView {
            VStack {
                Repositories()
            }
        }
    }
}

struct SecondView: View {
    var body: some View {
        NavigationView {
            VStack {
                About()
            }
        }
    }
}

struct ContentView: View {
    var body: some View {
        TabView {
            FirstView()
                .tabItem {
                    
                    Image(systemName: "house")
                    Text("Repositories")
                    
                    
                }
            
            SecondView()
                .tabItem {
                    Image(systemName: "person")
                    Text("About")
                }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
