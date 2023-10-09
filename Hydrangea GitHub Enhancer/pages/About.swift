//
//  AboutView.swift
//  Hydrangea GitHub Enhancer
//
//  Created by Acan on 2023/10/9.
//

import SwiftUI

struct About: View {
    
    var body: some View {
        NavigationView {
            ScrollView(showsIndicators: false) {
                VStack(alignment: .leading) {
                    
                    Divider()
                    
                    Text("Hydrangea GitHub Enhancer is a tool crafted by Acan to elevate your GitHub experience. It enhances the way you interact with repositories, providing easy access to project details.")
                        .padding(.bottom).padding(.top)
                    
                    Text("Features:")
                        .font(.headline)
                        .padding(.bottom)
                    
                    Text("• View a curated list of public repositories from a GitHub user.")
                        .padding(.bottom)
                    
                    Text("• Access project details, including names, links, and homepage information.")
                        .padding(.bottom)
                    
                    Text("• Navigate seamlessly through repositories with a clean and intuitive interface.")
                        .padding(.bottom)
                    
                    Text("Made with ❤️ by Acan.")
                        .padding(.bottom)
                    
                }.padding()
            }.navigationTitle(Text("About"))
        }
        
    }
}
