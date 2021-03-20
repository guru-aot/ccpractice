export interface AuthorState {
  authorList: AuthorModel[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
}
export interface AuthorModel {
  created: string;
  first_name: string;
  id: string;
  last_name: string;
  middle_name: string;
  modified: string;
}
