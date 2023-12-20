import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { INews } from "../models/INews";


export const newsApi = createApi({
  reducerPath: "newsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
    prepareHeaders: (headers) => {
      const token = JSON.parse(localStorage.getItem('user') || '{}')?.access_token;
      if (token) {
        headers.set('Authorization', `Bearer ${token}`);
      }
      return headers;
    },
  }),
  endpoints: (builder) => ({
    getAllNews: builder.query<any, string>({
      query: () => ({
        url: `/get/news_guardian`,
      })
    }),
    getNewsById: builder.query<any, number>({
      query: (id) => ({
        url: `/get/news_guardian/${id}`,
      })
    }),
    getNewsByDate: builder.query<any, { start_date: string, end_date: string }>({
      query: ({ start_date, end_date }) => ({
        url: `/get/news_guardian_${start_date}_${end_date}`,
      })
    }),
    deleteAllNews: builder.mutation<any, number>({
      query: () => ({
        url: `/delete/news`,
        method: "DELETE",
      })
    }),
    deleteNewsById: builder.mutation<any, number>({
      query: (id) => ({
        url: `/delete/news/${id}`,
        method: "DELETE",
      })
    }),
  }),
});

export const { useGetAllNewsQuery, useGetNewsByIdQuery, useGetNewsByDateQuery, useDeleteAllNewsMutation, useDeleteNewsByIdMutation } = newsApi;