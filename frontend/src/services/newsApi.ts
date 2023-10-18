import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { INews } from "../models/INews";

export const newsApi = createApi({
  reducerPath: "newsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
    prepareHeaders: (headers, { getState }) => {
      const token = JSON.parse(localStorage.getItem('user') || '{}')?.access_token;
      if (token) {
        headers.set('Authorization', `Bearer ${token}`);
      }
      return headers;
    },
  }),
  endpoints: (builder) => ({
    getAllNews: builder.query<INews[], string>({
      query: (param) => ({
        url: `/api/test_${param}`,
      })
    }),
    getNews: builder.query<INews, number>({
      query: (id) => ({
        url: `/api/test/${id}`,
      })
    }),
    postAllNews: builder.mutation<INews[], { param: string, request: string }>({
      query: ({ param, request }) => ({
        url: `/search/test_message_date_${param}`,
        method: "POST",
        body: request
      })
    }),
    postAllNewsMessage: builder.mutation<INews[], { param: string, message: string}>({
      query: ({param, message}) => ({
        url: `/search/test_message_${param}`,
        method: "POST",
        body: {message: message}
      })
    }),
  }),
});

export const { useGetAllNewsQuery, useGetNewsQuery, usePostAllNewsMessageMutation, usePostAllNewsMutation } = newsApi;